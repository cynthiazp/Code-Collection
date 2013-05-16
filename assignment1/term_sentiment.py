import sys
import json

tweet = sys.argv[2]
sent = sys.argv[1]

def tweet_list(tweet_file):


    term = {}
    filename = open(tweet_file)
    for line in filename:
        term[line] = json.loads(line)

    #print term.items()
    return term

    

def sent_dict(sent_file):

    
    scores = {} # initialize an empty dictionary

    filename = open(sent_file)
    for line in filename:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def main():
    tweets = tweet_list(tweet)
    #print tweets
    sentiment = sent_dict(sent)
    #print sentiment


    tweet_sentiment = {}
    
    score = {}
    for line in tweets:
        sum_sentiment = 0.0
        count = 0.0
        term = []
        if tweets[line].has_key("text"):
            for word in tweets[line]["text"].split():
                if not sentiment.has_key(word):
                    term.append(word)
#                    print word
                    count += 1.0
                value = sentiment.get(word,0)
                #print value
                sum_sentiment = sum_sentiment + value
                
        if count == 0.0:
            average = 0.0
        else:
            average = float(sum_sentiment)/count
        for index in term:
            if score.has_key(index):
                score[index] = score[index]+average
            else:
                score[index] = average
        
    
                
    for i in score:
        print "%s \t %f" %(i,score[i])


        

if __name__ == '__main__':
    main()
