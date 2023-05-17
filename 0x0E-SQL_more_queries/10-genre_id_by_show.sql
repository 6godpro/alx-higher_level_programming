-- Lists all shows contained in hbtn_0d_tvshows that have at least
-- one genre linked.
-- Record should display: tv_shows.title - tv_show_genres.genre_id
-- in ascending order by tv_shows.title and tv_show_genres.genre_id.
SELECT show.title, genre.genre_id
FROM tv_shows AS show
INNER JOIN tv_show_genres AS genre
ON show.id = genre.show_id
ORDER BY show.title, genre.genre_id;
