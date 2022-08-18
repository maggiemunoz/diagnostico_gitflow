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

def top_users(json_file):
    all_users = {}

    i = 0
    tweet_info = load_json(json_file, i)

    while tweet_info != -1:
        if not tweet_info["user"]["username"] in all_users.keys():
            all_users[tweet_info["user"]["username"]] = 1
        else:
            all_users[tweet_info["user"]["username"]] += 1

        i += 1
        tweet_info = load_json(json_file, i)

    users = []

    for k, v in all_users.items():
        users.append([v, k])

    users.sort(reverse=True)
    return users[:10]

def top_days(json_file):
    all_days = {}

    i = 0
    tweet_info = load_json(json_file, i)

    while tweet_info != -1:
        if not tweet_info["date"][:10] in all_days.keys():
            all_days[tweet_info["date"][:10]] = 1
        else:
            all_days[tweet_info["date"][:10]] += 1

        i += 1
        tweet_info = load_json(json_file, i)

    days = []

    for k, v in all_days.items():
        days.append([v, k])

    days.sort(reverse=True)
    return days[:10]

def top_hashtags(json_file):
    all_hashtags = {}

    i = 0
    tweet_info = load_json(json_file, i)

    while tweet_info != -1:
        hashtags = []
        tweet = tweet_info["content"]
        ht = False
        hashtag = ""
        for c in tweet:
            if c == "#" and not ht:
                ht = True
                hashtag += c
            elif ht and c != " ":
                hashtag += c
            elif ht and c == " ":
                ht = False
                hashtags.append(hashtag)
                hashtag = ""

        for ht in hashtags:
            if not ht in all_hashtags.keys():
                all_hashtags[ht] = 1
            else:
                all_hashtags[ht] += 1

        i += 1
        tweet_info = load_json(json_file, i)

    hashtags = []

    for k, v in all_hashtags.items():
        hashtags.append([v, k])

    hashtags.sort(reverse=True)
    return hashtags[:10]

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

