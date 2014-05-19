__author__ = 'zhengqin'


class Solution(object):
    """
    Question: Write a function to compute a^b efficiently. (A and B are both positive)
    """

    def power_function(self, a, b):
        if b == 0:
            return 1
        elif b == 1:
            return a
        result = self.power_function(a, b/2)
        if b%2 == 0 :
            return result * result
        else:
            return result * result * a

s = Solution()
print(s.power_function(1.7,100))