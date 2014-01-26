import twitter
import logging
import datetime
import os
from random import choice


'''Authorization'''
def authenticate():
	#[TODO] Add authentication to your magic 8 ball user account
	api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='',access_token_secret='')

	return api

def find_latest_tweet_id(latest_file):
	latest_tweet_id = 0
	for line in latest_file:
		latest_tweet_id = int(line)
	return latest_tweet_id






if __name__== "__main__":

	#List of replies
	answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Better not tell you now', "Don't count on it", 'My reply is no', "My sources say no", 'Outlook not so good', "Very doubtful"]

	#File that holds the id of the last tweet read
	LATESTFILE = 'latest.txt'	
	os.chdir("") #[TODO] Add current directory path here
	latest_file = open(LATESTFILE)
	
	latest_tweet_id = find_latest_tweet_id(latest_file)
	api = authenticate()	
	statuses = api.GetMentions(since_id=latest_tweet_id)
	
	#reply to each new status
	status_times = []	
	for status in statuses:
		print status.id
		if status.id > latest_tweet_id and status.in_reply_to_status_id == None and status.user.screen_name.lower() != 'magic8all':

			#find user mentions and remove magic8all from it
			return_status = "@" + status.user.screen_name + " "
			for user in status.user_mentions:
				if (user.screen_name.lower() != 'magic8all'):
					return_status += "@" + user.screen_name + " "
			 
			api.PostUpdate(return_status + choice(answers),  in_reply_to_status_id=status.id)
			print "posted"
		status_times.append(status.id)
	if len(status_times) != 0:
		fp = open(LATESTFILE, 'w')
		fp.write(str(max(status_times)))
		fp.close()			
		
