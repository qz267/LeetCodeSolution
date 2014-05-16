__author__ = 'zhengqin'


class Solution(object):
    """
    Question: Write a function to find the smaller angle between the hour and minute hand on an analog clock.
    """

    def get_angle(self, hour, minute):
        a_h = float(360/12)
        a_h_m = float((360/12)/60)
        a_m = float(360/60)

        h = float(( hour % 12 ) * a_h + minute * a_h_m)
        m = float(minute * a_m)

        angle = abs(float(h-m))
        return min(angle, 360.0 - angle)

s = Solution()
print s.get_angle(hour=1, minute=28)


