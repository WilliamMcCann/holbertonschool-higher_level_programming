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
else:
  cnx.close()
