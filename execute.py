import pymysql

try:
  print('starting...')
  print()

  dbConn = pymysql.connect(
    host='nu-cs-msa-mysql.cb1xaky37wq8.us-east-2.rds.amazonaws.com', 
    port=3306,
    user='movielens-read-only', 
    passwd='abc123!!', 
    database='movielens')

  sql = 'select * from movies limit 10';

  dbCursor = dbConn.cursor()
  dbCursor.execute(sql)
  rows = dbCursor.fetchall()

  for row in rows:
    print(row)

  dbCursor.close()
  dbConn.close()

  print()
  print('done')

except Exception as e:
  print("**Error:", str(e))

