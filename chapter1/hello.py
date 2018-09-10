import string
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
