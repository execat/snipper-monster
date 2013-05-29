# Populated with words after calling prepare_wordlist()
words = []

# Levenshtein distance
# def lev(s, t, current_min):
def lev(s, t):
    len_s, len_t = len(s), len(t)

    if len_s == 0:
        return len_t
    if len_t == 0:
        return len_s

    if(s[len_s - 1] == t[len_t - 1]):
        cost = 0
    else:
        cost = 1

    # value = min(lev(s[:len_s-1], t, current_min - 1) + 1, lev(s, t[:len_t-1], current_min - 1) + 1, lev(s[:len_s-1], t[:len_t-1], current_min) + cost)

    # if value < current_min:
    #   current_min = value
    #   return value
    # else:
    #   return None
    return min(lev(s[:len_s-1], t) + 1, lev(s, t[:len_t-1]) + 1, lev(s[:len_s-1], t[:len_t-1]) + cost)

def levenshtein(a, b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n

    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]

def prepare_wordlist():
    # Use the /usr/share/dict/words (~120000 words) OR
    # The file containing top 5k words in English from http://www.englishclub.com/vocabulary/common-words-5000.htm OR
    # The file containing top 10k words in English from https://github.com/first20hours/google-10000-english
    # Difference is in the performance: 50k ~> 1s, 10k ~> 1 - 2s, words file ~> 10 - 12s per result

    # f1 = open('/usr/share/dict/words')
    f1 = open('words-5k')
    # f1 = open('words-10k')

    tmp_list = f1.readlines()
    wordlist = [f.replace('\n', '') for f in tmp_list]
    return wordlist

def correct(word):
    score_list = []
    current_min = 100

    for f in words:
        # score_list.append(lev(word, f))
        score_list.append(levenshtein(word, f))

    # Approach 1: Just one word suggestion
    print(words[score_list.index(min(score_list))])

    # Approach 2: For multiple word suggestions
    # min_occ = min(score_list)
    # print("Minimum of score_list: %s" % min_occ)
    # indices = [i for i, x in enumerate(score_list) if x == min_occ]
    # for index in indices:
    #    print(words[index])

if __name__ == "__main__":
    words = prepare_wordlist()

    # Alternative approaches: remove triple repetition like "sheeep" and replace it by 2 ("sheep")
    # Penalize words not in the string (peeple matches "peephole" and "people" currently, but penalizing the "h" greater will result in peephole having a greater score

    while True:
        word = input("Enter a word ('quit' to quit): ")
        if word == "quit":
            break
        correct(word.lower())
