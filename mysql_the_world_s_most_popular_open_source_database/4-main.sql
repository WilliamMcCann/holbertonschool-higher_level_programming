#List of all TVShows by all Genres ordered by genre name (A-Z)
\! echo "\nList of all TVShows by all Genres ordered by genre name (A-Z)?"
SELECT Genre.name AS 'Genre name', TVShow.name AS 'TVShow name'
FROM Genre
  LEFT JOIN TVShowGenre ON Genre.id=TVShowGenre.genre_id
  LEFT JOIN TVShow ON TVShowGenre.tvshow_id = TVShow.id
ORDER BY Genre.name
;


#Name of the pilot (first episode of the first season) of each TVShow ordered by TVShow name (A-Z)?
\! echo "\nName of the pilot (first episode of the first season) of each TVShow ordered by TVShow name (A-Z)?"
SELECT TVShow.name AS 'TVShow name', Episode.name AS 'Episode name'
FROM Episode
  JOIN Season on Episode.season_id=Season.id
  JOIN TVShow on Season.tvshow_id=TVShow.id
WHERE Season.number=1 && Episode.number=1
ORDER BY TVShow.name
;

#List of all Genres by all TVShows ordered by TVShow name (A-Z)
\! echo "\nList of all Genres by all TVShows ordered by TVShow name (A-Z)?"
SELECT TVShow.name AS 'TVShow name', Genre.name AS 'Genre name'
FROM TVShow
  RIGHT JOIN TVShowGenre on TVShow.id=TVShowGenre.tvshow_id
  RIGHT JOIN Genre on TVShowGenre.genre_id=Genre.id
ORDER BY TVShow.name ASC
;
