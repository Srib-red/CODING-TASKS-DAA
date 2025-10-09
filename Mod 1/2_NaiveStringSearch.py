def Naive_string_search(txt,pat):
    n = len(txt)
    m = len(pat)
    matches = []
    i = 0
    j = 0

    while i < n:
        if txt[i] == pat[j]:
            i = i + 1
            j = j + 1

            if j == m:
                matches.append(i-m)
                j = 0;

        else:
            i = i - j + 1
            j = 0

    return matches

if __name__ == "__main__":
    txt = (input("Enter a string, to search ##the## in string: "))  
    pat = "the"

    match_the_idx = Naive_string_search(txt,pat)
    print(match_the_idx)
