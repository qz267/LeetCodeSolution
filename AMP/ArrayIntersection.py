__author__ = 'zhengqin'


class Solution(object):
    """
    Question: Find the intersection of two unsorted integer arrays.
    """

    def array_intersection(self, s1, s2):
        return list(set(s1) & set(s2))


s1 = [1,2,2,2,3,4,5,63,4,56]
s2 = [2,3,4]

s = Solution()
print s.array_intersection(s1, s2)