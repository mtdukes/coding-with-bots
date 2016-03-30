'''
A template for the coding-with-bots class
'''
#import libraries
import tweepy
import random
from time import sleep

#establish keys as global variables,
#making them accessible within each function
secret_keys = []

#Our main worker function
def main():
	authenticate()
	#test_timeline()
	#a_tweet("HEY Y'ALL I'M A TWEET.")
	#tweet_ex()
	#random_tweet()
	gif_tweet()

#A function for authenticating into our Twitter app
def authenticate():
	#generate auth details and assign appropriately
	_get_secrets()
	consumer_key = secret_keys[0]
	consumer_secret = secret_keys[1]
	access_token = secret_keys[2]
	access_token_secret = secret_keys[3]

	#access our twitter app with the appropriate credentials
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	#create tweepy object
	global api
	api = tweepy.API(auth)

#a test function to see if all the authenticateion is working
def test_timeline():
	#get the current timeline and store in the public_tweets variable
	public_tweets = api.home_timeline()
	#for every tweet stored in the public_tweets variable, print out the tweet text
	for tweet in public_tweets:
		print tweet.text

# a basic tweet function that takes a value and tweets it
def a_tweet(status_upd):
	api.update_status(status_upd)

# a function to generate a random tweet
def random_tweet():
	# build a twitter list of five possible tweets
	tweet_list = [
	'Charm was a scheme for making strangers like and trust a person immediately, no matter what the charmer had in mind.',
	"There is no good reason good can't triumph over evil, if only angels will get organized along the lines of the mafia.",
	"Shrapnel was invented by an Englishman of the same name. Don't you wish you could have something named after you?",
	"If your brains were dynamite there wouldn't be enough to blow your hat off.",
	"And so on."
	]
	x = 0
	# create a loop to tweet twice
	while x < 2:
		try:
			# generate a random variable between 0 and 4
			rand = random.randint(0, 4)
			# use that random variable to grab an item from tweet_list
			api.update_status(tweet_list[rand])
			# take a 30-second break so we don't overwhelm our followers
			sleep(30)
			#increment our counter
			x += 1
		# if there's an error, catch it instead of crashing and print out the error message
		except tweepy.TweepError, e:
			print 'Error sending tweet:', e[0][0]['message']

# a function to tweet a gif
def gif_tweet():
	try:
		# takes a file location and a text string to update status
		api.update_with_media('../img/pulp-fiction-search.gif','BEHOLD, a gif')
	# if there's an error, catch it instead of crashing and print out the error message
	except tweepy.TweepError, e:
			print 'Error sending tweet:', e[0][0]['message']

# utility function for retrieving secret keys
# from our secret key file
def _get_secrets():
	# global here allows the code to update the global variable
	# for all functions
	global secret_keys
	# open the .keys file and read each line into our secret_keys list
	with open('../.keys') as f:
		secret_keys = f.read().splitlines()

if __name__ == '__main__':

	print "Running twitter app..."

	# run the main function
	main()

	print "All done! Thanks for tweeting."