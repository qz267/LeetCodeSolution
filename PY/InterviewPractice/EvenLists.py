__author__ = 'zheng'


class Solution(object):
    """
    Question: Given an unsorted, even-numbered array of integers, divide the array into two lists of the equal sizes
    such that their total is as close as possible

    Example:
    input {1000,500,200,1,5,10,50,70,70,100} output:
                    List 1 : 500, 200, 100, 70, 70, List 2 : 1000, 50, 10, 5, 1,

    input {50,10,200,150,900,250,40,50,950,5,90,80,60,600}
                    List 1: 900, 600, 90, 60, 50, 10, 5,
                    List 2: 950, 250, 200, 150, 80, 50, 40,
    """

    def make_lists(self, original_list):
        temp = original_list
        temp.sort()
        result, l1, l2 = [], [], []
        sum1, sum2 = 0, 0
        length = len(temp)
        for i in temp:
            if sum1 < sum2 and len(l1) < length/2:
                l1.append(i)
                sum1 += i
            else:
                l2.append(i)
                sum2 += i
        result.append(l1)
        result.append(l2)

        return result



l = [1000,500,200,1,5,10,50,70,70,100]
l2 = [50,10,200,150,900,250,40,50,950,5,90,80,60,600]

s = Solution()
print s.make_lists(original_list=l2)