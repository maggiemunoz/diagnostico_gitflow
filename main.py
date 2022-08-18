import sys
import json

def top_retweeted(json):
    pass

def top_users(json):
    pass

def top_days(json):
    pass

def top_hashtags(json):
    pass

def load_json(file_name, n):
    file = open(file_name)
    lineas = file.readlines()
    if n < len(lineas):
        data = json.loads(lineas[n])
        file.close()
        return data
    else:
        file.close()
        return -1


def main(name, json_file):
    data = load_json(json_file, 0)
    print(data)
    print(type(data))
    print(name(data))


if __name__ == "__main__":
        
    name = sys.argv[1]
    json_file = sys.argv[2]

    main(locals()[name], json_file)

