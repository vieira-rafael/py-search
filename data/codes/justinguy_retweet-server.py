import osimport tweepyfrom flask import Flaskfrom two1.lib.wallet import Walletfrom two1.lib.bitserv.flask import Paymentfrom retweet_settings import *
app = Flask(__name__)wallet = Wallet()payment = Payment(app, wallet)
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)api = tweepy.API(auth)me = api.me()

@app.route('/info')@payment.required(INFO_PRICE)def info(): return "\n______\n\nThis endpoint is for Twitter account @%s which has %d followers.\nYou can purchase a follow from @%s for %d satoshi by calling \n/follow/YOUR_TWITTER_HANDLE or a retweet for %d satoshi at /retweet/TWEET_ID or a favorite for %d satoshi at /favorite/TWEET_ID.\n______\n" % (me.screen_name, me.followers_count, me.screen_name, FOLLOW_PRICE, RETWEET_PRICE, FAVORITE_PRICE)

@app.route('/follow/<acct_name>')@payment.required(FOLLOW_PRICE)def follow(acct_name):        res = api.create_friendship(acct_name) return "@%s was successfully followed by @%s" % (acct_name, me.screen_name)

@app.route('/favorite/<int:tweet_id>')@payment.required(FAVORITE_PRICE)def favorite(tweet_id):    res = api.create_favorite(tweet_id) return "Tweet successfully favorited by @%s" % (me.screen_name)

@app.route('/retweet/<int:tweet_id>')@payment.required(RETWEET_PRICE)def retweet(tweet_id):        res = api.retweet(tweet_id) return "Successfully retweeted by @%s (https://twitter.com/%s)" % (me.screen_name, me.screen_name)

if __name__ == '__main__':    zt_ip = os.popen('/sbin/ifconfig zt0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1').read().strip() print("-----") print("Server starting, to get info from any 21BC1 use:") print("21 buy --maxprice {price} url http://{ip}:{port}/info".format( price = INFO_PRICE, ip = zt_ip, port = SERVER_PORT    )) print("-----")    app.run(host='0.0.0.0', port=SERVER_PORT)