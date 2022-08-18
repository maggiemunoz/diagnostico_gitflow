import sys
import json

def top_retweeted(json_file):
    i = 0
    tweet_info = load_json(json_file, i)
    while tweet_info != -1:
        print(tweet_info["retweetCount"])

        i += 1
        tweet_info = load_json(json_file, i)

    return "hola"

    pass

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

