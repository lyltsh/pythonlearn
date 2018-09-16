# 保留最后N个元素
from collections import deque


def serach(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


# yield 生成器函数

# example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in serach(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
