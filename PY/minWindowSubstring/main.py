# Minimum Window Substring
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, return
# the emtpy string "".

# If there are multiple such windows, you are guaranteed that there will
# always be only one unique minimum window in S.

'''
Created on 2013-5-16
@author: Yubin Bai
'''
from collections import Counter


def minWindow(s, t):
    target = Counter(t)
    current = {}
    for i in target:
        current[i] = 0
    leftMin, rightMin, currMin = 0, 0, 1 << 33
    left = right = 0
    for right in range(len(s)):
        if s[right] in target:
            current[s[right]] += 1
        if all([current[x] >= target[x] for x in target]):
            while left <= right:
                if s[left] not in target:
                    left += 1
                elif current[s[left]] - target[s[left]] >= 1:
                    current[s[left]] -= 1
                    left += 1
                else:  # cannot shorten more
                    break
            if currMin >= right - left + 1:
                leftMin, rightMin, currMin = left, right, right - left + 1

    return s[leftMin:rightMin + 1]

if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    print(minWindow(S, T))
