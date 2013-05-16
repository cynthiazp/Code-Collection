import sys
import json
import operator

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
twees_list. Count the occurrence of the hash tags.
'''
	tweet = sys.argv[1]

    	tweets = tweet_list(tweet)
	count = 0.0
	tag_count = {}
	for line in tweets:
		if (tweets[line].has_key("entities") and tweets[line]["entities"].has_key("hashtags") and tweets[line]["entities"]["hashtags"] != []):
			for attr in tweets[line]["entities"]["hashtags"]:
#				print attr["text"]
				tag = attr["text"]
				if tag_count.has_key(tag) :
					tag_count[tag] += 1.0
				else :
					tag_count[tag] = 1.0
	tag_count = sorted(tag_count.iteritems(), key=operator.itemgetter(1), reverse=True)
	size = 10
	if len(tag_count) < 10 :
		size = len(tag_count)
	for i in range(size) :
		print tag_count[i][0]+" "+str(tag_count[i][1])

if __name__ == '__main__':
	main()
