import clipboard
import webbrowser

long_tweet = clipboard.get()

tweet_length = 140
tweet_prefix = '...'
tweet_postfix = '...'
tweet_counter = '(x/y)'

def balance_tweets (tweets, num_chars, max_num_chars):

	num_tweets = len(tweets)

	return tweets

def pad_tweets (tweets):

	padded_tweets = []
	for tweet in tweets:

		padded_tweet = ''

		if (tweets.index(tweet) != 0):
			padded_tweet = '... '

		if (len(padded_tweet) != 0):
			padded_tweet = padded_tweet + ' '

		padded_tweet = padded_tweet + tweet

		if (tweets.index(tweet) < len(tweets) - 1):
			padded_tweet = padded_tweet + '...'

		padded_tweet = padded_tweet + ' (' + str(tweets.index(tweet) + 1) + '/' + str(len(tweets)) + ')'

		padded_tweets.append(padded_tweet)

	return padded_tweets

# If the character count <= 140,
# return the text.
if len(long_tweet) <= 140:
	print [long_tweet]
	exit

# How many chars per tweet?
num_chars = len(long_tweet)

# How many characters can we support per tweet?
max_num_chars = tweet_length - len(tweet_prefix) - len(tweet_postfix) - len(tweet_counter) - 4

# Array to hold the tweets
tweets = ['']

# Build the tweets
i = 0
for word in long_tweet.split(' '):
	if (len(tweets[i]) + len(word) > max_num_chars):
		tweets.append(word)
		i = i + 1
	else:
		if (len(tweets[i]) > 0):
			tweets[i] = tweets[i] + ' '
		tweets[i] = tweets[i] + word

print tweets

# Load balance the tweets
tweets = balance_tweets(tweets, num_chars, max_num_chars)

# Add the textual padding to the tweets
tweets = pad_tweets(tweets)

# Done! Return the split tweet.
clipboard.set('|%^|'.join(tweets))
webbrowser.open('workflow://')
