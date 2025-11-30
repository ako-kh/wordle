from random import randint
import sys
from time import sleep

def to_dict(string):
    """
    :param string:
    :return dict:
    """
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
    """
    :param w1:
    :param w2:
    :return string:
    """
    string = ["_" for _ in range(len(w2))]
    w1_dict = to_dict(w1)
    w2_dict = to_dict(w2)

    if w1 == w2:
        return "^" * len(w2)
    for k in w2_dict:
        try:
            if w1_dict[k] == w2_dict[k]:
                # if all the repetitions of the letter
                # are in the correct place...
                for i in w2_dict[k]["index"]:
                    string[i] = "^"
            elif w1_dict[k]["count"] >= w2_dict[k]["count"]:
                # in case of fewer repetitions of letter in w2
                # we must mark status (^,!) of all repetitions in w2
                for i in w2_dict[k]["index"]:
                    if i in w1_dict[k]["index"]:
                        string[i] = "^"
                    else:
                        string[i] = "!"
            else:
                # in case of more repetitions of letter in w2
                # we must mark status (^,!) of correct number of repetitions
                start = w2_dict[k]["count"] - w1_dict[k]["count"]
                for i in w2_dict[k]["index"]:
                    if i in w1_dict[k]["index"]:
                        string[i] = "^"
                    elif start > 0:
                        start -= 1
                    else:
                        string[i] = "!"
        except KeyError:
            pass

    return "".join(string)

def my_print(*args, end="\n"):
    print("      ",end="")
    for i in args:
        print(i,end="")
    print(end,end="")

def main():
    with open("words.txt", "r") as f:
        words = f.readlines()
        word = words[randint(0, len(words))].rstrip("\n")
        # print(word)

    tries = 6
    print(
        f"In WORDLE you got {tries} to guess the word.\n\n"
        "Each guess must be a valid 5-letter word.\n\n"
        "under your guess will appear next three simbols:\n"
        "   '^' meaning the letter is in correct spot\n"
        "   '!' meaning the letter is in the word but not in correct spot\n"
        "   '_' meaning the letter is not in the word\n"
    )
    while True:
        if 0 >= tries:
            my_print(f"The word was {word}")
            break

        input_w = input("word: ")
        if "life+" == input_w:
            tries += 2
        elif 5 != len(input_w):
            print(f'word must be 5 letters long')
            sleep(3)
            sys.stdout.write("\x1b[2F")
            sys.stdout.write("\x1b[0J")
            continue
        elif input_w + "\n" not in words:
            print(f'"{input_w}" is not a valid word')
            sleep(3)
            sys.stdout.write("\x1b[2F")
            sys.stdout.write("\x1b[0J")
            continue

        tries -= 1
        result = compare(word, input_w)

        sys.stdout.write("\x1b[1F")
        sys.stdout.write("\x1b[0J")
        sys.stdout.flush()
        my_print(input_w)
        my_print(result, end="")
        my_print(f"tries left: {tries}")

        if "^^^^^" == result:
            my_print("YOU WON")
            break

if __name__ == '__main__':
    main()