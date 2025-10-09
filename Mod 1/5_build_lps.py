def get_lps(s):
    n = len(s)
    lps = n*[0]

    i = 1
    j = 0

    while i < n:
        if s[i] == s[j]:
            j = j + 1
            lps[i] = j
            i = i + 1
        elif j > 0:
            j = lps[j-1]
        else:
            i = i+1
    
    return lps

if __name__ == "__main__":

    s1 = "ABCBCABC"
    #lps: 00000123
    print(get_lps(s1))