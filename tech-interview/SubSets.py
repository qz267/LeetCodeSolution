__author__ = 'zhengqin'


class Solution(object):
    """
    Question: Find all subsets of a set.

    Example:
    input:{abcd}
    output:{} {d} {b} {c} {a} {bc} {da} {ca} {dc} {db} {ba} {dbca} {bca} {dba} {dca} {dbc}
    input: {a,b}
    output: {}{a}{b}{a,b}
    input: {a,b,c}
    output: {}{a}{b}{c}{a,b}{a,c}{b,c}{a,b,c}
    """

    def sub_sets(self, s):
        result = [[]]
        for x in s:
            result += [y + [x] for y in result]
        return result


s = Solution()
result = s.sub_sets(s="abcd")
print(result)
print len(result)