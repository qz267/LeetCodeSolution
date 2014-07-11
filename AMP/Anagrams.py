__author__ = 'zhengqin'


class Solution(object):
    """
    Question: Write an algorithm to determine whether two strings are anagrams or not.
    """

    def is_anagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        else:
            return 2[::-1] == s1

s1 = "123"
s2 = "3241"

s = Solution()
print(s.is_anagrams(s1,s2))
