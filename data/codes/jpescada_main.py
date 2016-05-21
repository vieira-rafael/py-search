#!/usr/bin/env python
# import external modules
import atexit
from config import *from models import tweetfrom controllers import twitter_clientfrom controllers import tweet_reader



def goodbye(): print "See you later!"	tweet_reader.cleanup() # twitter_client.cleanup()

atexit.register(goodbye)

# run default processif __name__ == '__main__':
 print "Bot starting... Press Ctrl+C to stop."
	tweet.initialize()
	tweet_reader.initialize()
	twitter_client.initialize()
 

 


