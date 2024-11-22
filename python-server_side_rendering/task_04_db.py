#!/usr/bin/python3
"""
This module will be used to extend dynamic data display
to include SQLite in Flask
"""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_data = data.get("items")
    except FileNotFoundError:
        data = []

    return render_template('items.html', items=item_data)


@app.route('/products', methods=['GET'])
def display_products():
    source = request.args.get('source', '')
    product_id = request.args.get('id', type=int)
    message = None
    products = []

    if source not in ['json', 'csv', 'sql']:
        message = "Wrong source"

    try:
        if source == 'json':
            with open('products.json', 'r') as file:
                products = json.load(file)

        elif source == 'csv':
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]

        elif source == 'sql':
            con = sqlite3.connect("products.db")
            cur = con.cursor()

            if product_id:
                print(f"Executing query: SELECT * FROM Products WHERE id = {product_id}")
                query = "SELECT * FROM Products WHERE id = ?"
                cur.execute(query, (product_id,))
            else:
                query = "SELECT * FROM Products"
                cur.execute(query)

            products = [
                {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]
                 } for row in cur.fetchall()]
            con.close()
            print(f"Products fetched: {products}")

        if product_id:
            products = [
                product for product in products if product['id'] == product_id]
            print(f"Filtered Products: {products}")
            if not products:
                message = "Product not found."

    except FileNotFoundError:
        message = "File not found."

    except Exception as e:
        message = f"An error occurred: {e}"

    return render_template('product_display.html', products=products, message=message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)