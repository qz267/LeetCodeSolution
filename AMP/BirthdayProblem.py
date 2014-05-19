__author__ = 'zhengqin'


class Solution(object):
    """
    Question: Find the probability that, given n people, a pair of them will have the same birthday.
    (Based off the Birthday Paradox)
    """

    def birthday_problem(self, n):
        np = 1.0
        for i in range(n):
            np *= ((365.0 - float(i))/365.0)
        return 1 - np

s = Solution()
print(s.birthday_problem(364))