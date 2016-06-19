#number of seasons ordered by name
\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT TVShow.name, COUNT(Season.number) AS nb_seasons
FROM TVShow, Season
WHERE TVShow.id = Season.tvshow_id
GROUP BY TVShow.name
ORDER BY TVShow.name ASC
;

#Network by TVShow by name
\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT TVShow.name AS "TVShow Name", Network.name AS "Network Name"
FROM TVShow, Network
WHERE TVShow.network_id = Network.id
ORDER BY TVShow.name
;

#Fox shows in alpha order
\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT TVShow.name
FROM TVShow JOIN Network
ON TVShow.network_id = Network.id
WHERE Network.name='FOX (US)'
;

#Number of episodes of TVShows ordered by name (A-Z)
\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT TVShow.name, count(Season.tvshow_id) AS nb_episodes
FROM TVShow
  JOIN Season on TVShow.id=Season.tvshow_id
  JOIN Episode on Season.id=Episode.season_id
GROUP BY Season.tvshow_id
ORDER BY TVShow.name ASC
;
