# Sherlock and Anagrams(https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_r=internal-search)
def sherlockAndAnagrams(s):
    count=0
    # the different lengths a substring could have, from "1 to len(s)-1"
    # the last number is excluded, so the end of the range is "len(s)" instead of "len(s)-1"
    for shift in range(1, len(s)):
        # if a substring contains only one letter, indices for the substring would be "i:i+1",
        # until the end of the string, the indices would be "len(s)-1:len(s)"
        # if a substring contains two letters, indices for the substring would be i:i+2
        # until the end of the string, the indices would be "len(s)-2:len(s)"
        # ...
        # the last number is excluded, so the end of the range is "len(s)-shift+1" instead of "len(s)-shift"
        sub_strings = [s[i:i+shift] for i in range(len(s)-shift+1)]

        # sort all the substrings to identify substrings that have the same letters
        sub_strings_sorted = [sorted(ss) for ss in sub_strings]
        for i in range(len(sub_strings_sorted) - 1):
            for j in range(i+1, len(sub_strings_sorted)):
                if sub_strings_sorted[i] == sub_strings_sorted[j]:
                    count += 1
    return(count)