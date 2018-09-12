import re

print(re.search(r'w*.', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

line = "Cats are smarter than dogs";
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
print(searchObj.groups())

phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print(num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print(num)


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'AB234SLD98SD'
print(re.sub('(?P<value>\d+)', double, s))

pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
print(pattern.match('one12twothree34four'))  # 查找头部，没有匹配
print(pattern.match('one12twothree34four', 2, 10))  # 从'e'的位置开始匹配，没有匹配
print(pattern.match('one12twothree34four', 3, 10).groups(0))  # 从'1'的位置开始匹配，正好匹配

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())


#split
print(re.split('\W+', 'runoob, runoob, runoob.'))


