from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


    
    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        cur = self.conn.cursor()
        #Insert

        insert_string = '''INSERT INTO tweetwordcount (word,count) VALUES (%s, 1)'''
        isFirstWord = True
        try:
            # self.log("***INSERT***")
            # self.log(insert_string.format(word))
            cur.execute(insert_string, (word,));
            self.conn.commit() 
        except Exception as e:
            isFirstWord = False
            
        # self.log("\n")
        update_string = '''UPDATE tweetwordcount SET count = count + 1 WHERE word=%s '''

        if not isFirstWord:
            try:
                # self.log("***UPDATE***")
                # self.log(update_string.format(word))
                cur.execute(update_string, (word,))
                self.conn.commit()
            except Exception as e:
                self.log("update didn't work")
                self.log(e)
                self.log("\n")

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        # self.log('%s: %d' % (word, self.counts[word]))
