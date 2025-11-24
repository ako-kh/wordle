from random import randint
import sys

def to_dict(string):
    str_dict = {}

    for i in range(len(string)):
        c = string[i]
        try:
            str_dict[c]["index"].append(i)
            str_dict[c]["count"] += 1
        except KeyError:
            str_dict[c] = {
                "index": [i],
                "count": 1
            }
    return str_dict


def compare(w1, w2):
    string = ["_","_","_","_","_"]
    w1_dict = to_dict(w1)
    w2_dict = to_dict(w2)

    if w1 == w2:
        return w2
    for k in w2_dict:
        try:
            if w1_dict[k] == w2_dict[k]:
                for i in w2_dict[k]["index"]:
                    string[i] = k
            elif w1_dict[k]["count"] >= w2_dict[k]["count"]:
                for i in w2_dict[k]["index"]:
                    if i in w1_dict[k]["index"]:
                        string[i] = k
                    else:
                        string[i] = k.upper()
            else:
                start = w2_dict[k]["count"] - w1_dict[k]["count"]
                for i in w2_dict[k]["index"]:
                    if i in w1_dict[k]["index"]:
                        string[i] = k
                    elif start > 0:
                        start -= 1
                    else:
                        string[i] = k.upper()
        except KeyError:
            pass

    return "".join(string)

def main():
    with open("words.txt", "r") as f:
        words = f.readlines()
        word = words[randint(0, len(words))].rstrip("\n")
        print(word)

    while True:
        s = compare(word, input("word: "))
        sys.stdout.write("\x1b[1F")
        sys.stdout.write("\x1b[0J")
        print("     ", s)
        sys.stdout.flush()

if __name__ == '__main__':
    main()