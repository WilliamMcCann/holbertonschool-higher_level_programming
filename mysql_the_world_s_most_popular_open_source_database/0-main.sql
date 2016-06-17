#lists tables
\! echo "\nList of all tables?"
SHOW TABLES;

#shows table structures
\! echo "\nDisplay the table structure of TVShow, Genre and TVShowGenre?"
SHOW CREATE TABLE TVShow;
SHOW CREATE TABLE TVShowGenre;
SHOW CREATE TABLE Genre;

#lists TVShows
\! echo "\nList of TVShows, only id and name ordered by name (A-Z)?"
SELECT id, name
FROM TVShow
ORDER BY name ASC;

#lists Genres
\! echo "\nList of Genres, only id and name ordered by name (Z-A)?"
SELECT id, name
FROM Genre
ORDER BY name DESC;

#Lists networks
\! echo "\nList of Network, only id and name?"
SELECT id, name
FROM Network;

#lists number of episodes
\! echo "\nNumber of episodes in the database?"
SELECT COUNT(id)
FROM Episode;
