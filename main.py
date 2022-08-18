import sys
import json

def top_retweeted(json_file):
    i = 0
    tweet_info = load_json(json_file, i)

    top_10_tweets = []
    top_10_rts = []

    min_rts_top = 10000000000
    min_top = ""

    while tweet_info != -1:
        rts = tweet_info["retweetCount"]
        if len(top_10_tweets) == 10:
            if rts > min_rts_top:
                top_10_tweets.remove(min_top)
                top_10_rts.remove(min_rts_top)
                
                top_10_tweets.append(tweet_info)
                top_10_rts.append(rts)
                
                min_rts_top = min(top_10_rts)
                
                for elem in top_10_tweets:
                    if elem["retweetCount"] == min_rts_top:
                        min_top = elem
                        break
    
        else:
            top_10_tweets.append(tweet_info)
            top_10_rts.append(tweet_info["retweetCount"])
            
            if tweet_info["retweetCount"] < min_rts_top:
                min_rts_top = tweet_info["retweetCount"]
                min_top = tweet_info

        i += 1
        tweet_info = load_json(json_file, i)

    return top_10_tweets

def top_users(json):
    pass

def top_days(json):
    pass

def top_hashtags(json):
    pass

def load_json(lineas, n):
    if n < len(lineas):
        data = json.loads(lineas[n])
        return data
    else:

        return -1


def main(name, json_file):
    file = open(json_file)
    lineas = file.readlines()

    print(name(lineas))
    file.close()


if __name__ == "__main__":
        
    name = sys.argv[1]
    json_file = sys.argv[2]

    main(locals()[name], json_file)

