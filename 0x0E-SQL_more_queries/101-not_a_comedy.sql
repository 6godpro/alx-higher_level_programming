-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT s.title
     FROM tv_shows AS s
         LEFT JOIN tv_show_genres AS tsg
         ON s.id = tsg.show_id
	 LEFT JOIN tv_genres AS g
	 ON g.id = tsg.genre_id
	 WHERE s.title NOT IN (
	     SELECT s.title
	         FROM tv_shows AS s
		     LEFT JOIN tv_show_genres AS tsg
		     ON tsg.show_id = s.id
		     LEFT JOIN tv_genres AS g
		     ON g.id = tsg.genre_id
	             WHERE g.name = 'Comedy')
    GROUP BY s.title
    ORDER BY s.title;
