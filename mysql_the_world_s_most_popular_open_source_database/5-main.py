#!/usr/bin/env python

#fetch TVShows, Seasons and Episodes of the MySQL database and display them*/

import mysql.connector

try:
  cnx = mysql.connector.connect(user='student',
                                password='aLQQLXGQp2rJ4Wy5',
                                host='173.246.108.142',
                                database='Project_169')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

c = cnx.cursor()

c.execute("SELECT TVShow.name FROM TVShow")
Shows = c.fetchall()
for name in Shows:
    print name[0] + ":"

    c.execute("SELECT Season.number FROM Season")
    Seasons = c.fetchall()
    for season in Seasons:
        print "\tSeason " + str(season) + ":"

        c.execute("SELECT Episode.name, Episode.number FROM Episode")
        Episodes = c.fetchall()
        for episode in Episodes:
            print "\t\t" + str(episode)

'''
            for show in Shows:
    print TVShow.name[0] + ':'
    for season in Seasons:
        print 'Season ' + '[1]' + ':'
        for episodeName in Episodes:
            print Episode.number + ': ' + Episode.name

for (TVShow.name) in c:
  print("{}:{:%b}".format(
    TVShow.name))
'''

c.close()
cnx.close()
