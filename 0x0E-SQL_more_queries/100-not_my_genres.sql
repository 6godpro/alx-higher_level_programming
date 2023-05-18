-- List all genres not linked to the show Dexter.
SELECT g.name
    FROM tv_genres AS g
        INNER JOIN tv_show_genres AS tsg
	ON g.id = tsg.genre_id
	INNER JOIN tv_shows AS ts
	ON ts.id = tsg.show_id
	WHERE g.name NOT IN (
	         SELECT g.name FROM tv_genres AS g
		     INNER JOIN tv_show_genres AS tsg
		     ON g.id = tsg.genre_id
		     INNER JOIN tv_shows AS s
		     ON s.id = tsg.show_id
		     WHERE s.title = 'Dexter'
		     )
    GROUP BY g.name
    ORDER BY g.name;
