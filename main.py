import twitter
import os
import sys
import time


def get_api(consumer_key, consumer_secret, access_token_key, access_token_secret):
    print("API connected.")
    time.sleep(2)
    return twitter.Api(consumer_key=api_key,
                    consumer_secret=api_secret_key,
                    access_token_key=token_access,
                    access_token_secret=token_secret)

# Search : 180/15m // Tweet : 300/3H

api = get_api(api_key, api_secret_key, token_access, token_secret)
tweets = 0
searchs = 0
limitTweets = 300
limitSearchs = 180

def endsWith(sentence, keyword):
    return sentence.endswith(keyword)

def tweet(update, reply_id):
    global tweets
    tweets += 1
    api.PostUpdate(update, reply_id)

def search(research, howMany):
    global searchs
    searchs += 1
    searchResults = api.GetSearch(raw_query="q="+research+"&result_type=recent&count="+howMany)
    for search in searchResults:
        if(endsWith(search.text, "oui") or endsWith(search.text, "oui ?") or endsWith(search.text, "oui !")):
            print(search.text)
            tweet("@" + search.user.screen_name + " stiti", search.id)

def main():
    global searchs
    global tweets
    global limitTweets
    global limitSearchs
    stop = False
    while(not stop):
        try:
            search("oui", "100")
        except:
            stop = True
        if(searchs >= limitSearchs):
            stop = True
        elif(tweets >= limitTweets):
            stop = True
        print(f"tweet = {str(tweets)}")
        time.sleep(5)

if __name__ == "__main__":
    main()