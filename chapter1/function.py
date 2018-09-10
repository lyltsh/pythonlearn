# 类型属于对象，变量是没有类型的
def printme(str):
    print(str)
    return


printme("你好，这是打印数据")
list_temp = [1243, 'adf', '09sdf']
printme(list_temp)


# 变参
def printinfo(arg1, *vartuple):
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfo(10)
print(10, [1, 2, 34, 'adfa'])
