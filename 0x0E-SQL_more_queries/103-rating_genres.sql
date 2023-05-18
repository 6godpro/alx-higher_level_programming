-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
SELECT g.name, SUM(rate) AS rating
    FROM tv_genres AS g
        LEFT JOIN tv_show_genres AS tsg
	ON tsg.genre_id = g.id
	LEFT JOIN tv_shows AS s
	ON s.id = tsg.show_id
	LEFT JOIN tv_show_ratings AS r
	ON s.id = r.show_id
    GROUP BY g.name
    ORDER BY rating DESC;
