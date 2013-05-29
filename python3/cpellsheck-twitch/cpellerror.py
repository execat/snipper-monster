# cpellerror.py
import random, sys
words = []

def prepare_wordlist():
    # Use the /usr/share/dict/words (~120000 words) OR
    # The file containing top 5k words in English from http://www.englishclub.com/vocabulary/common-words-5000.htm OR
    # The file containing top 10k words in English from https://github.com/first20hours/google-10000-english
    worlist = []
    f1 = open('words-5k')

    alist = f1.readlines()
    wordlist = [f.replace('\n', '') for f in alist]

    return wordlist

def create():
    # Pull out a random word
    word = random.choice(words)
    word_list = list(word)

    # Capitalize a random word... twice!
    i = random.randrange(0, len(word_list))
    word_list[i] = word_list[i].upper()
    i = random.randrange(0, len(word_list))
    word_list[i] = word_list[i].upper()

    # Repeat a random word... twice!
    i = random.randrange(0, len(word_list))
    word_list.insert(i, word_list[i])
    i = random.randrange(0, len(word_list))
    word_list.insert(i, word_list[i])

    # Change a vowel
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i, a in enumerate(word_list):
        if a in vowels:
            flip_vowel = random.randint(0, 1) # Binary conditional
            if flip_vowel:
                # Randomly change vowel if flip_vowel = 1
                word_list[i] = random.choice(vowels)

    # Return word and the error word
    return (word, "".join(word_list))

if __name__ == "__main__":
    words = prepare_wordlist()
    i = 0
    while i < 500:
        tup = create()
        sys.stderr.write(tup[0] + "\n") # Actual words are written to stderr
        sys.stdout.write(tup[1] + "\n") # Error words are written to stdout
        i = i + 1
    print("quit")            # Program ends abruptly if EOF is encountered