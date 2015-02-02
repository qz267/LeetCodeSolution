__author__ = 'zhengqin'


class Solution(object):
    """
    Question: In Java, the String class includes the function contains(CharSequence s) that returns true if
    the string contains the given sequence of values. Given two strings, write a function to determine if one
    string is a rotation of another string.
    Example:
    input: {"computerscience","tersciencecompu"} output: true
    """

    def string_rotation(self, s1, s2):
        # print s1 == s2[::-1]
        return sorted(s1) == sorted(s2)
        # return s1 == s2[::-1]


s = Solution()
s1 = "computerscience"
s2 = "tersciencecompu"
print s.string_rotation(s1, s2)