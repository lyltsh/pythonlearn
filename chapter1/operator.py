

print(function.printme("hello function"))

# if,else
flag = False
name = 'lle'
if name == 'python':
    flag = True
    print('welcome boss')
else:
    print(name)

"使用and和or表示条件"
num = 10
if num > 0 and num < 12:
    print(num)
else:
    print("not num")

for letter in 'python':
    print(letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print(fruit)

for index in range(len(fruits)):
    print('当前水果:' + fruits[index])

for num in range(10, 20):
    for i in range(2, num):
        if (num % i == 0):
            j = num / i
            print("%d = %d * %d" % (num, i, j))
            break
    else:
        print(str(num) + "是一个质数")

#100以内的素数
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i, " 是素数")
    i = i + 1

print("Good bye!")


