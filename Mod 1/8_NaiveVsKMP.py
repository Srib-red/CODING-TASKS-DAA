def Naive_string_search(txt,pat):
    n = len(txt)
    m = len(pat)
    matches = []
    i = 0
    j = 0
    comparsion_naive = 0

    while i < n:
        if txt[i] == pat[j]:
            comparsion_naive = comparsion_naive + 1
            i = i + 1
            j = j + 1

            if j == m:
                matches.append(i-m)
                j = 0;
        else:
            i = i - j + 1
            j = 0

    if len(matches) == 0:
        print("No Matches found.\n")
    else:
        print("Match found at starting index ###from Naive Search###: ", matches)

    return comparsion_naive

def get_lps(s):
    n = len(s)
    lps = n*[0]
    comparsion_lps = 0

    i = 1
    j = 0
    while i < n:
        if s[i] == s[j]:
            comparsion_lps = comparsion_lps + 1;
            j = j + 1
            lps[i] = j
            i = i + 1
        elif j > 0:
            j = lps[j-1]
        else:
            i = i+1
    
    return lps, comparsion_lps

def kmp_algo(txt, pat):
    n = len(txt)
    m = len(pat)
    matched_idx = [];
    lps, com_lps  = get_lps(pat)
    comparison_kmp = 0

    if m > n: return -1
    
    i = 0
    j = 0
    while i < n:
        if txt[i] == pat[j]:
            comparison_kmp = comparison_kmp + 1
            j = j + 1
            i = i + 1
            if j == m:
                j = lps[j-1]
                matched_idx.append(i - m)
        elif j > 0:
            j = lps[j-1]
        else:
            i = i + 1
    
    if len(matched_idx) == 0:
        print("No Matches found.\n")
    else:
        print("Match found at starting index ###from KMP###: ", matched_idx)
    
    return comparison_kmp, com_lps

if __name__ == "__main__":
    txt1 = "AAAAAAAAAAABBCDDAAACAAABBB"
    pat1 = "AAABB"

    com_kmp, com_lps1 = kmp_algo(txt1, pat1)
    com_naive = Naive_string_search(txt1, pat1)

    print("Comparisons for LPS TABLE BUILDING: ", com_lps1, " comparisons")
    print("KMP VS NAIVE: ", com_kmp," comparisons", " VS ", com_naive, " comparisons")

