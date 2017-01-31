import sqlite3 #library

DB = sqlite3.connect("dbname=Cookies") #connect to the DB, name of DB (hostname, )

cursor = DB.cursor() # create object CURSOR that runs the query and fetches results,

cursor.execute( # execute the query
  "select host_key from cookies limit 10")

results = cursor.fetchall() # fetch results and use to scan the results

print results

conn.close #always close connection esp if there's a loop
