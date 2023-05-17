-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Record should display: tv_shows.title - tv_show_genres.genre_id
-- In ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
WHERE g.show_id is NULL
ORDER BY s.title, g.genre_id;
