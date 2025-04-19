
-- 1. Top 10 Highest Rated Titles (with at least 100,000 votes)
CREATE VIEW top_10_highest_rated_titles AS
SELECT t.primary_title, r.average_rating, r.num_votes
FROM titles t
JOIN ratings r ON t.tconst = r.tconst
WHERE r.num_votes >= 100000
ORDER BY r.average_rating DESC
LIMIT 10;

-- SELECT Example:
-- SELECT * FROM top_10_highest_rated_titles;

-- 2. People who are both Directors and Writers
CREATE VIEW directors_and_writers AS
SELECT DISTINCT d.nconst
FROM title_directors d
JOIN title_writers w ON d.tconst = w.tconst AND d.nconst = w.nconst;

-- SELECT Example:
-- SELECT * FROM directors_and_writers;

-- 3. Most Common Professions (Top 5)
CREATE VIEW top_5_professions AS
SELECT profession, COUNT(*) AS count
FROM professions
GROUP BY profession
ORDER BY count DESC
LIMIT 5;

-- SELECT Example:
-- SELECT * FROM top_5_professions;

-- 4. Titles with More Than 1 Genre
CREATE VIEW multi_genre_titles AS
SELECT t.tconst, t.primary_title, COUNT(g.genre_id) AS genre_count
FROM titles t
JOIN genres g ON t.tconst = g.tconst
GROUP BY t.tconst
HAVING COUNT(g.genre_id) > 1
ORDER BY genre_count DESC;

-- SELECT Example:
-- SELECT * FROM multi_genre_titles;

-- 5. Top 5 Genres by Average Rating
CREATE VIEW top_5_genres_by_rating AS
SELECT gl.genre, AVG(r.average_rating) AS avg_rating
FROM genres g
JOIN genre_lookup gl ON g.genre_id = gl.genre_id
JOIN ratings r ON g.tconst = r.tconst
GROUP BY gl.genre
ORDER BY avg_rating DESC
LIMIT 5;

-- SELECT Example:
-- SELECT * FROM top_5_genres_by_rating;

-- 6. Titles with More than One Known For Person
CREATE VIEW titles_with_multiple_known_people AS
WITH known_count AS (
  SELECT tconst, COUNT(nconst) AS num_people
  FROM known_for
  GROUP BY tconst
)
SELECT t.primary_title, kc.num_people
FROM known_count kc
JOIN titles t ON kc.tconst = t.tconst
WHERE kc.num_people > 1
ORDER BY kc.num_people DESC;

-- SELECT Example:
-- SELECT * FROM titles_with_multiple_known_people;

-- 7. Rank Top Titles per Genre
CREATE VIEW ranked_titles_per_genre AS
SELECT t.primary_title, gl.genre, r.average_rating,
       RANK() OVER (PARTITION BY gl.genre ORDER BY r.average_rating DESC) AS genre_rank
FROM titles t
JOIN ratings r ON t.tconst = r.tconst
JOIN genres g ON t.tconst = g.tconst
JOIN genre_lookup gl ON g.genre_id = gl.genre_id
WHERE r.num_votes > 10000;

-- SELECT Example:
-- SELECT * FROM ranked_titles_per_genre WHERE genre_rank = 1;

-- 8. Actors or Actresses with More Than 5 Principal Credits
CREATE VIEW frequent_actors AS
SELECT p.primary_name, COUNT(*) AS appearances
FROM principals pr
JOIN people p ON pr.nconst = p.nconst
WHERE pr.category IN ('actor', 'actress')
GROUP BY p.primary_name
HAVING COUNT(*) > 5
ORDER BY appearances DESC;

-- SELECT Example:
-- SELECT * FROM frequent_actors;

-- 9. Count of Titles per Genre
CREATE VIEW title_count_by_genre AS
SELECT gl.genre, COUNT(*) AS total_titles
FROM genres g
JOIN genre_lookup gl ON g.genre_id = gl.genre_id
GROUP BY gl.genre;

-- SELECT Example:
-- SELECT * FROM title_count_by_genre;

-- 10. Average Runtime of Movies per Genre
CREATE VIEW avg_runtime_per_genre AS
SELECT gl.genre, AVG(t.runtime_minutes) AS avg_runtime
FROM titles t
JOIN genres g ON t.tconst = g.tconst
JOIN genre_lookup gl ON g.genre_id = gl.genre_id
WHERE t.runtime_minutes IS NOT NULL
GROUP BY gl.genre;

-- SELECT Example:
-- SELECT * FROM avg_runtime_per_genre;

-- 11. Longest Runtime Title per Genre
CREATE VIEW longest_runtime_per_genre AS
SELECT gl.genre, t.primary_title, t.runtime_minutes
FROM titles t
JOIN genres g ON t.tconst = g.tconst
JOIN genre_lookup gl ON g.genre_id = gl.genre_id
WHERE t.runtime_minutes IS NOT NULL
AND t.runtime_minutes = (
  SELECT MAX(t2.runtime_minutes)
  FROM titles t2
  JOIN genres g2 ON t2.tconst = g2.tconst
  WHERE g2.genre_id = g.genre_id
);

-- SELECT Example:
-- SELECT * FROM longest_runtime_per_genre;

-- 12. Titles by People Born After 1950
CREATE VIEW titles_by_young_creators AS
SELECT DISTINCT t.primary_title, p.primary_name, p.birth_year
FROM titles t
JOIN title_directors d ON t.tconst = d.tconst
JOIN people p ON d.nconst = p.nconst
WHERE p.birth_year > 1950;

-- SELECT Example:
-- SELECT * FROM titles_by_young_creators;

-- 13. People Who Directed and Acted in Same Title
CREATE VIEW directed_and_acted AS
SELECT DISTINCT p.primary_name, t.primary_title
FROM principals pr
JOIN title_directors td ON pr.tconst = td.tconst AND pr.nconst = td.nconst
JOIN titles t ON t.tconst = pr.tconst
JOIN people p ON p.nconst = pr.nconst
WHERE pr.category IN ('actor', 'actress');

-- SELECT Example:
-- SELECT * FROM directed_and_acted;

-- 14. Average Rating by Title Type
CREATE VIEW avg_rating_by_title_type AS
SELECT t.title_type, AVG(r.average_rating) AS avg_rating
FROM titles t
JOIN ratings r ON t.tconst = r.tconst
GROUP BY t.title_type;

-- SELECT Example:
-- SELECT * FROM avg_rating_by_title_type;

-- 15. Most Voted Titles in Each Genre
CREATE VIEW most_voted_per_genre AS
SELECT gl.genre, t.primary_title, r.num_votes
FROM titles t
JOIN ratings r ON t.tconst = r.tconst
JOIN genres g ON t.tconst = g.tconst
JOIN genre_lookup gl ON g.genre_id = gl.genre_id
WHERE (gl.genre, r.num_votes) IN (
  SELECT gl2.genre, MAX(r2.num_votes)
  FROM genres g2
  JOIN genre_lookup gl2 ON g2.genre_id = gl2.genre_id
  JOIN ratings r2 ON g2.tconst = r2.tconst
  GROUP BY gl2.genre
);

-- SELECT Example:
-- SELECT * FROM most_voted_per_genre;

-- 16. Find Titles Without Any Genre
CREATE VIEW titles_without_genre AS
SELECT t.tconst, t.primary_title
FROM titles t
LEFT JOIN genres g ON t.tconst = g.tconst
WHERE g.tconst IS NULL;

-- SELECT Example:
-- SELECT * FROM titles_without_genre;

-- 17. Titles with Most Known For Entries
CREATE VIEW titles_with_most_known_for AS
SELECT t.tconst, t.primary_title, COUNT(k.nconst) AS total_known_for
FROM known_for k
JOIN titles t ON k.tconst = t.tconst
GROUP BY t.tconst
ORDER BY total_known_for DESC
LIMIT 10;

-- SELECT Example:
-- SELECT * FROM titles_with_most_known_for;

-- 18. Titles That Are Both TVSeries and Have Ratings
CREATE VIEW rated_tv_series AS
SELECT t.primary_title, r.average_rating
FROM titles t
JOIN ratings r ON t.tconst = r.tconst
WHERE t.title_type = 'tvSeries';

-- SELECT Example:
-- SELECT * FROM rated_tv_series;

-- 19. Number of Episodes per Series
CREATE VIEW episode_count_per_series AS
SELECT e.parent_tconst, COUNT(*) AS episode_count
FROM episodes e
GROUP BY e.parent_tconst;

-- SELECT Example:
-- SELECT * FROM episode_count_per_series;

-- 20. Top 5 Most Credited People in Principals
CREATE VIEW top_5_principal_people AS
SELECT p.primary_name, COUNT(*) AS credits
FROM principals pr
JOIN people p ON pr.nconst = p.nconst
GROUP BY p.primary_name
ORDER BY credits DESC
LIMIT 5;

-- SELECT Example:
-- SELECT * FROM top_5_principal_people;
