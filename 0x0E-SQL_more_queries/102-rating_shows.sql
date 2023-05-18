-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
SELECT s.title, SUM(rate) AS rating
    FROM tv_shows AS s
        LEFT JOIN tv_show_ratings AS r
        ON s.id = r.show_id
    GROUP BY s.title
    ORDER BY rating;
