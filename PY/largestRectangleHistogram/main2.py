__author__ = 'zheng'


def largestRectangle(data):
    largest = 0
    def cal(height, data):
        wide = 0
        temp = 0
        for s in data:
            if s >= height:
                temp += 1
                if temp > wide:
                    wide = temp
            else:
                temp = 0
        return wide*height
    h = 1
    while cal(h, data) != 0:
        temp = cal(h, data)
        if temp > largest:
            largest = temp
        h += 1
    return largest

if __name__ == '__main__':
    array = [2, 1, 5, 6, 2, 3]
    print largestRectangle(array)