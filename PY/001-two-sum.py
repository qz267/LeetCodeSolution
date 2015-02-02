class Solution:
# @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        numbers = sorted(num)
        length = len(num)
        left = 0
        right = length - 1
        index = []
        while left < right: 
            sums = numbers[left] + numbers[right]
            if sums == target:
                for i in range(length):
                    if num[i] == numbers[left]:
                        index.append(i + 1)
                    elif num[i] == numbers[right]:
                        index.append(i + 1)
                    if len(index) == 2:
                        break
                break
            elif sums > target:
                right -= 1
            else:
                left += 1
                result = tuple(index)
        return result
