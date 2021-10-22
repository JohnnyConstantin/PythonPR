import json
import random

def main():
    for x in range (1,5):
        dict = {"interface": x, "data": random.random()*x}
        jsonstring = json.dumps(dict, indent=3)
        print(jsonstring)


if __name__ == '__main__':
    main()
