
from mysql import connector
from mysql.connector import errorcode
import mysql.connector



def func():
  try:
    connection_ = connector.connect(
      user="root",
      password="",
      host="127.0.0.1",
      database="tidal"
    )
    return connection_
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
    return False
  else:
    connection_.close()
    return False
  