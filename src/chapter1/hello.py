import sys
import cmath
import random

print(cmath.sqrt(-1))
print(cmath.log10(100))
print(cmath.sin(1))

print(random.choice(range(10)))
print(random.randrange(1, 20, 3))

list_sample = ['1232', 13, 'abcls']
shuffle_list = random.shuffle(list_sample)
print(list_sample)
print(shuffle_list)

print(random.uniform(2, 90))

# 格式化输出
print("My name is %s and weight is %d kg!" % ('Zara', 21))

hi_str = '''hi
there'''
print(hi_str)

str_sample = "strSample_s"
print(str_sample.capitalize())
print(str_sample.center(20))
print(str_sample.count('s', 0, len(str_sample)))
print(str_sample.endswith('ss', 0, len(str_sample)))

x = 'robb'
sys.stdout.write(x + '\n')

s = 'abcdef'
print(s[1:5])
print(s[1:])

"可以从后面索引"
print(s[-6:])

"加号（+）是字符串连接运算符，星号（*）是重复操作"
str_sample = 'Hello World!'
print(str_sample)  # 输出完整字符串
print(str_sample[0])  # 输出字符串中的第一个字符
print(str_sample[2:5])  # 输出字符串中第三个至第五个之间的字符串
print(str_sample[2:])  # 输出从第三个字符开始的字符串
print(str_sample * 2)  # 输出字符串两次
print(str_sample + "TEST")  # 输出连接的字符串

"列表，list"
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)
"加号 + 是列表连接运算符，星号 * 是重复操作"
list_sample = ['runoob', 786, 2.23, 'john', 70.2]
tiny_list = [123, 'john']
print(list_sample)  # 输出完整列表
print(list_sample[0])  # 输出列表的第一个元素
print(list_sample[1:3])  # 输出第二个至第三个元素
print(list_sample[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tiny_list * 2)  # 输出列表两次
print(list_sample + tiny_list)  # 打印组合的列表

"""
元组是另一个数据类型，类似于List（列表）。
元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
"""
tuple_sample = ('runoob', 786, 2.23, 'john', 70.2)
tiny_tuple = (123, 'john')
print(tuple_sample)
print(tuple_sample[0])
print(tuple_sample[1:3])
print(tuple_sample[2:])
print(tiny_tuple * 2)
print(tuple_sample + tiny_tuple)

"元组是不允许更新的。而列表是允许更新的"
# tuple_sample[0] = '122'
list_sample[0] = '123'

'''
Python 字典
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict_sample = {}
dict_sample['one'] = "This is one"
dict_sample[2] = "This is two"
tiny_dict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict_sample['one'])
print(dict_sample[2])
print(dict_sample.keys())
print(tiny_dict)
print(tiny_dict.keys())
print(tiny_dict.values())

"tuple：将序列转成一个元祖"
tuple_list = tuple(list_sample)
print(tuple_list)
"list: 将序列转成一个list"
list_tuple = list(tuple_sample)
print(list_tuple)
