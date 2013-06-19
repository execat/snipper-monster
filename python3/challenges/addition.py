def sum_of(a):
    addition = 0
    for f in a:
        addition = addition + int(f)
    return addition        

def getEqualSumSubstring (s):
    string_s = str(s)
    success = False
    ans = 0
    for i in range(0, len(string_s)):
        for j in range(i, len(string_s) + 1):
            diff = j - i
            offset = int(diff / 2)
            #print("Main: " + string_s[i:j])
            #print("A: " + string_s[i:i+offset], sum_of(string_s[i:i+offset]))
            #print("B: " + string_s[i+offset:j], sum_of(string_s[i+offset:j]))
            if (sum_of(string_s[i:i+offset]) == sum_of(string_s[i+offset:j])) and (sum_of(string_s[i:i+offset]) > ans):
                success = True
                ans = sum_of(string_s[i:i+offset])
                print("Main: " + string_s[i:j])
                print("A: " + string_s[i:i+offset], sum_of(string_s[i:i+offset]))
                print("B: " + string_s[i+offset:j], sum_of(string_s[i+offset:j]))
                #print(i, j)
            
    if success:
        return ans
    else:
        return 0
   
print(getEqualSumSubstring(123231))
print(getEqualSumSubstring(986561517416921217551395112859219257312))
