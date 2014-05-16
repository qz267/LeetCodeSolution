__author__ = 'zhengqin'


class Solution(object):
    """
    Question: Find the longest common substring between two texts.
    """

    def longest_common_substring(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        result = ""
        for i in range(l1):
            match = ""
            for j in range(l2):
                if i + j < l1 and s1[i+j] == s2[j]:
                    match += s2[j]
                else:
                    if len(match) > len(result):
                        result = match
                    else:
                        match = ""
        return result

    def lcs(self, xstr, ystr):
        if not xstr or not ystr:
            return ""
        x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
        if x == y:
            return x + self.lcs(xs, ys)
        else:
            return max(self.lcs(xstr, ys), self.lcs(xs, ystr), key=len)


s1 = "ABCDE"
s2 = "ABAABCAABBBCDE"

s = Solution()
print(s.longest_common_substring(s1, s2))
print(s.lcs(s1, s2))