from DS.Hash_Tables.hash_tables import Hashtable
import re


def repeat_word(text):
    reg = r'\S+'
    valid_chars = re.findall(reg, text)
    print(valid_chars)
    words = "".join([i for i in text.lower() if i in valid_chars])
    print(words)
    hashs = Hashtable()
    for i in words.split():
        if hashs.contains(i):
            return i
        hashs.set(i, "i")

    return "No Repeated Word Found"


if __name__ == '__main__':
    t = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness"
    print(repeat_word(t))


