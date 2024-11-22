fetch('https://swapi-api.hbtn.io/api/films/?format=json').then(response => response.json()).then(data => {
  const movies = data.results;
  const list = document.getElementById('list_movies');

  movies.forEach((movies) => {
    items = document.createElement('li');
    items.textContent = movies.title;
    list.appendChild(items);
  });
});
