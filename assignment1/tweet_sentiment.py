import sys
import json



def tweet_list(tweet_file):
    ''' (file) -> list of dictionaries
This method should take your output.txt
file and create a list of dictionaries.
'''
    term = {}
    filename = open(tweet_file)
    for line in filename:
        term[line] = json.loads(line)
 

    #print term.items()
    return term

    

def sent_dict(sent_file):
    ''' (file) -> dictionary
This method should take your sentiment file
and create a dictionary in the form {word: value}
'''
    
    scores = {} # initialize an empty dictionary

    filename = open(sent_file)
    for line in filename:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

    
def main():
    
    sent = sys.argv[1]
    tweet = sys.argv[2]
    
    tweets = tweet_list(tweet)
    #print tweets
    sentiment = sent_dict(sent)
    #print sentiment
    
    '''Create a method below that loops through each tweet in your
twees_list. For each individual tweet it should add up you sentiment
score, based on the sent_dict.
'''
    tweet_sentiment = {}
    for line in tweets:
        sum_sentiment = 0.0
        
        if (tweets[line] and tweets[line].has_key("text")):
            
            for word in tweets[line]["text"].split():

                value = sentiment.get(word,0.0)
                #print value
                sum_sentiment = sum_sentiment + value

            tweet_sentiment[word] = sum_sentiment
            #print float(sum_sentiment)

    
    for result in tweet_sentiment:
        print tweet_sentiment[result]
    
    #print tweet_sentiment.len()
    
        

    
if __name__ == '__main__':
    main()
