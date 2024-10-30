-- 13. This script will lists all genres from the database named hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show_genres.name genres, COUNT(*) number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.name = tv_show_genres.genre_id
GROUP BY tv_genres
ORDER BY tv_genres;