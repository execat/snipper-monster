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
