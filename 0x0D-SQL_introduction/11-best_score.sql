-- Lists all records with a score >= 10 in the table second_table
   -- Results should display both the score and the name.
   -- Records should be ordered by score.
SELECT score, name FROM second_table WHERE score>10 ORDER BY score DESC;
