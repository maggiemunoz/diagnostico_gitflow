import sys

def top_retweeted(json):
    pass

def top_users(json):
    pass

def top_days(json):
    pass

def top_hashtags(json):
    pass


def main(name, json):
    print(name(json))


if __name__ == "__main__":
        
    name = sys.argv[1]
    json = sys.argv[2]

    main(locals()[name], json)

