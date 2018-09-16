import time

print(time.time())
local_time = time.localtime(time.time())
print(local_time)
print(local_time.tm_yday)

# 获取格式化的时间
local_time = time.asctime(time.localtime(time.time()))
print(local_time)

# 使用 time 模块的 strftime 方法来格式化日期
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2018"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
