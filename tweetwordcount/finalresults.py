#Sample code snippets for working with psycopg


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

def printAll():
  #Connecting to tcount
  conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

  cur = conn.cursor()

  #Select
  cur.execute("SELECT word, count from tweetwordcount")
  records = cur.fetchall()

  sorted_records =  sorted(records)

  for record in sorted_records:
    print record
  conn.commit()

  conn.close()

def printWord(word):
  conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

  cur = conn.cursor()

  #Select
  cur.execute("SELECT count from tweetwordcount where word=%s", (word,))
  records = cur.fetchall()

  count = records[0][0]
  sorted_records =  sorted(records)

  print """Total number of occurrences of of "{}": {}""".format(word, count)
  conn.commit()

  conn.close()

if __name__ == '__main__':

  if len(sys.argv) > 1:
    word = sys.argv[1]
    printWord(word)

  else:
    printAll()
