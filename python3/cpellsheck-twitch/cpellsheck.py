# Populated with words after calling prepare_wordlist()
words = []

# Levenshtein distance
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

    return min(lev(s[:len_s-1], t) + 1, lev(s, t[:len_t-1]) + 1, lev(s[:len_s-1], t[:len_t-1]) + cost)

# http://hetland.org/coding/python/levenshtein.py
# More efficient implementation
def levenshtein(a, b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0]*n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]

def prepare_wordlist():
    f1 = open('/usr/share/dict/words')

    tmp_list = f1.readlines()
    wordlist = [f.replace('\n', '') for f in tmp_list]
    return wordlist

def correct(word):
    score_list = []
    current_min = 100

    for f in words:
        score_list.append(levenshtein(word, f))

words = prepare_wordlist()
