# cpellsheck.py
# Populated with words after calling prepare_wordlist()
words = {}

def process_word(word):
    # Lowercase
    word.lower()

    # Remove repetitions
    ulist = []
    # [ulist.append(f) AND prev = f for f in word if f not prev]
    prev = ''
    ulist = []

    for f in word:
        if f is not prev:
            ulist.append(f)
            prev = f

    # Remove vowels
    prev = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    vlist = []
    for f in ulist:
        if f not in vowels:
            vlist.append(f)
            prev = None
        elif prev is not '*':
            vlist.append('*')
            prev = '*'

    return ''.join(vlist)

def prepare_wordmap():
    # Use the /usr/share/dict/words (~120000 words) OR
    # The file containing top 5k words in English from http://www.englishclub.com/vocabulary/common-words-5000.htm OR
    # The file containing top 10k words in English from https://github.com/first20hours/google-10000-english
    wordmap = {}
    f1 = open('words-5k')

    alist = f1.readlines()
    blist = [f.replace('\n', '') for f in alist]

    for f in blist:
        wordmap[process_word(f)] = f
    return wordmap

def correct(word):
    if word in words.values():
        return word
    if word not in words:
        word = process_word(word)
        if word in words.keys():
            return words[word]
        else:
            return 'NO SUGGESTION'

if __name__ == "__main__":
    words = prepare_wordmap()

    while True:
        word = input("> ")
        if word == "quit":
            break
        print(correct(word.lower()))
