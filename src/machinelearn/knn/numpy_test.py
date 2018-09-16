import operator
import numpy as np

array_one = np.ones([3, 10])
print(array_one)
print('==================')

# 均匀分布
random_one = np.random.rand(3, 10)
print(random_one)
print(random_one.shape)
print('==================')

uniform_one = np.random.uniform(0, 10, 20)
print(uniform_one)
print('==================')

int_one = np.random.randint(0, 10, 20)
print(int_one)
print('==================')

# 正态分布
arr = np.random.normal(1.75, 0.1, (4, 5))
print(arr)
# 截取第1至2行的第2至3列(从第0行算起)
after_arr = arr[1:3, 2:4]
print(after_arr)
print('==================')

# tile
a = np.array([3, 4, 2])
print(a)
print(a.shape)
print(a.ndim)
b = np.tile(a, [3, 1])
print(b)
print(b.shape)
print(b.ndim)
print(b.argsort())
print('==================')

# sorted
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# 以年龄作为key排序
sorted_student = sorted(student_tuples, key=lambda student: student_tuples[2], reverse=True)
print(sorted_student)
# key使用operator，可以以两个维度进行排序，优先选择
sorted_student = sorted(student_tuples, key=operator.itemgetter(1, 2), reverse=True)
print(sorted_student)

