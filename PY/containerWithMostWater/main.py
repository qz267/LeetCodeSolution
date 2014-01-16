# Given n non-negative integers a1, a2, ..., an, where each represents a
# point at coordinate (i, ai). n vertical lines are drawn such that the
# two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
# together with x-axis forms a container, such that the container contains
# the most water.

# Note: You may not slant the container.


def maxArea(heights):
    left, right = 0, len(heights) - 1
    currMax = min(heights[left], heights[right]) * (right - left)
    while left < right:
        currMax = max(currMax, min(heights[left], heights[right]) * (right - left))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return currMax

print maxArea([2, 4, 1, 3])
