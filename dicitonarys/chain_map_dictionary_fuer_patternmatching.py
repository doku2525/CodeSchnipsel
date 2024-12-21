from collections import ChainMap
import re


if __name__ == "__main__":
    dic_eins = {"pe": 10, "pb": 20}
    dic_zwei = {r"c\+\d+": 200, r"c-\d+": -200, r"c=\d+": 500}

    for key, value in dic_zwei.items():
        if re.match(key, 'c+1'):
            print(f" {value = }")