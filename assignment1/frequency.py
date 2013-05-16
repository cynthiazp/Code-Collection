import sys
import json

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
	tweet = sys.argv[1]

    	tweets = tweet_list(tweet)
	count = 0.0
	tweet_count = {}
	for line in tweets:
		if (tweets[line].has_key("text")):
#			print tweets[line]["text"]
			for word in tweets[line]["text"].split():
				count += 1.0
				if tweet_count.has_key(word) :
					tweet_count[word] += 1.0
				else :
					tweet_count[word] = 1.0
				
	for word in tweet_count:
		p = tweet_count[word]/count	        
		print word+" "+str(p)

if __name__ == '__main__':
	main()
