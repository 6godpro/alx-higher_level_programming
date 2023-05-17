-- Lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
-- * If a show doesn’t have a genre, display NULL in the genre column
-- * Each record should display: tv_shows.title - tv_genres.name
-- * Must be sorted in ascending order by the show title and genre name
SELECT s.title, tg.name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS tsg
ON s.id = tsg.show_id
LEFT JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY s.title, tg.name;
