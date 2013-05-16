import sys
import json
import operator
import re

def tweet_list(tweet_file):
	''' (file) -> list
This method will take tweet file and
create a list of dictionaries from it.
'''
	files = open(tweet_file)
	terms = {}
	for line in files:
		terms[line] = json.loads(line)

	return terms

def sent_dict(sent_file):
	''' (file) -> dictionary
This method will take sentiment file and
create a dictionary in the form {word: value}
'''
	afinnfile = open(sent_file)
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		# The file is tab-delimited. "\t" means "tab character"
		term, score = line.split("\t")
		# Convert the score to an integer.
		scores[term] = int(score)

#	print scores.items() # Print every (term, score) pair in the 	
	return scores

def main():
	'''The main method is going to loops through each tweet in the
twees_list. For each individual tweet it should add up the sentiment
score, based on the sentiment list.
'''

	sent = sys.argv[1]
	tweet = sys.argv[2]

    	tweets = tweet_list(tweet)
	sentiment = sent_dict(sent)

	states = {}
	for line in tweets:
		sum_sentiment = 0.0
		
		if tweets[line].has_key("place") and tweets[line]["place"] != None:
		        if (tweets[line]["place"].has_key("full_name")
		        and tweets[line]["place"]["country_code"] == "US"):
		                if tweets[line].has_key("text"):
		    
		                        for word in tweets[line]["text"].split():
		                                value = sentiment.get(word,0.0)
		                                sum_sentiment = sum_sentiment + value
		                
				state = tweets[line]["place"]["full_name"][-2:]
				sub = re.match( r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]+', state)
				if sub :
					state = sub.group()
				        if state in states:
						states[state] += sum_sentiment
				        else:
						states[state] = sum_sentiment
		                     
	happy_states = sorted(states.items(), key=operator.itemgetter(1), reverse = True)
	print happy_states[0][0]


if __name__ == '__main__':
	main()
