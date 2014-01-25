import twitter

if __name__== "__main__":

	#log configuration
	logging.basicConfig(filename='/home/faizan/magic8all/log.txt', level=logging.INFO)
	now = datetime.datetime.now()
	#File that holds the id of the last tweet read
	LATESTFILE = 'latest.txt'	
	os.chdir("/home/faizan/magic8all")
	#Authentication
	api = twitter.Api(consumer_key='Dmq6ujtXIEA2N2RO8CCBw', consumer_secret='wVe9p6vWaTxg5lIuSzjN5sNMOUJUxQx52o0WGSVa6jQ', access_token_key='1321505791-44SyvpFjmQT3fdkxZcv4PvJtVVctmJw0Y3m63gW',access_token_secret='bCzIxyQ4Z8jzaqnxckpDUglhlLD5Ql9Z0xTiqz5WYc')
	#List of replies
	answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Better not tell you now', "Don't count on it", 'My reply is no', "My sources say no", 'Outlook not so good', "Very doubtful"]
	
	
