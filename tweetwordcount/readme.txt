# NOTE -- this guide assumes use of UCB ami-d4dd4ec3, that the 
# setup script has been run, and that postgres is running

Install psycopg
-- pip install psycopg2==2.6.2
Install tweepy
-- pip install tweepy

Ensure postgres is running
-- ps axf | grep postgres

If necessary, set up postgres using UCB provided setup script

Make the database and table
-- python make_database_and_table.py


Update twitter credentials in /src/spouts/tweets.py. For example, add:
twitter_credentials = {
    "consumer_key"        :  "xxxxxxx",
    "consumer_secret"     :  "xxxxxxx",
    "access_token"        :  "xxxxxxx",
    "access_token_secret" :  "xxxxxxx",
}

From /tweetwordcount, 
-- sparse run