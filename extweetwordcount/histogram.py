#Sample code snippets for working with psycopg


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

def printHistogram(low, high):
  #Connecting to tcount
  conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

  cur = conn.cursor()

  #Select
  cur.execute("SELECT word, count from tweetwordcount where count >= %s and count <= %s", (low, high))
  records = cur.fetchall()

  sorted_records =  sorted(records, key=lambda x : x[1])

  for record in sorted_records:
    print record
  conn.commit()

  conn.close()


if __name__ == '__main__':

  range_str = sys.argv[1]
  print range_str
  bounds = [x.strip() for x in range_str.split(',')]

  low = bounds[0]
  high = bounds[1]

  printHistogram(low, high)