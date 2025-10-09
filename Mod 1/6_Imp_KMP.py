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

def kmp_algo(txt, pat):
    n = len(txt)
    m = len(pat)
    matched_idx = [];
    lps = get_lps(pat)

    if m > n: return -1
    
    i = 0
    j = 0
    while i < n:
        if txt[i] == pat[j]:
            j = j + 1
            i = i + 1
            if j == m:
                j = lps[j-1]
                matched_idx.append(i - m)
                print("Match Found!!! at starting_idx: ", i-m)
        elif j > 0:
            j = lps[j-1]
        else:
            i = i + 1
    
    if len(matched_idx) == 0:
        print("No Matches found.\n")
    else:
        print("Match found at starting index: ", matched_idx)
    
    return 0

if __name__ == "__main__":
    txt1 = "CATSABCBCABCDOGSABCBCABC"
    pat1 = "ABCBCABC"

    kmp_algo(txt1, pat1)