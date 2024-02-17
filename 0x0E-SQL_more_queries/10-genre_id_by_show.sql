-- lists all shows contained
SELECT tv_shows.title, tv_show_genres.genre_id
FROM  tv_shows
JOIN tv_shows_genres
ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title AND tv_show_genres.genre_id;