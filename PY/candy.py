__author__ = 'zheng'


class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if (ratings == [] or ratings is None):
            return 0
        ratings.sort()
        cur = ratings[0]
        bench_mark = 1
        total = 0
        for i in ratings:
            if i == cur:
                total += bench_mark
            elif i > cur:
                bench_mark += 1
                total += bench_mark
                cur = i
        return total
