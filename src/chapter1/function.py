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

# 格式化输出
print("{}@{}".format("1223", "233"))

"""
匿名函数
python 使用 lambda 来创建匿名函数。
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
"""
sum_sample = lambda arg1, arg2: arg1 + arg2;
print(sum_sample(12, 9))


import math
content = dir(math)
print(content)





