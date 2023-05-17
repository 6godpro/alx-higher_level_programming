-- Lists all genres of the show Dexter in the database.
SELECT g.name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tsg
ON g.id = tsg.genre_id
INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
WHERE ts.title = 'Dexter';
