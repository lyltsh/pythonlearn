import subprocess

"""
subprocess模块用来创建新的进程，连接到其stdin、stdout、stderr管道并获取它们的返回码。
subprocess模块的出现是为了替代如下旧模块及函数：os.system、os.spawn*、os.popen*、popen2.*、commands.*
"""
# subprocess demo

res = subprocess.run("ls")
print(res)

print(subprocess.run("ls -ltr", shell=True))

print(subprocess.run(["ls", "-l"]))

print(subprocess.run("echo hello", shell=True))

# run another python file
"""
注意不要为stdout和stderr参数赋值subprocess.PIPE，如果子进程输出量较多会造成死锁，
这两个参数可以赋值为subprocess.STDOUT打印到屏幕或者赋值为一个文件对象将输出写入文件：
"""
# subprocess.call("python3 run.py", shell=True)
subprocess.call("python3 run.py", shell=True, stdin=open('fake_input', 'r'), stdout=open('result', 'w'))

# check_call
try:
    res = subprocess.check_call(["ls", "("])
    print("res:", res)
except subprocess.CalledProcessError as exc:
    print("return_code", exc.returncode)
    print("cmd", exc.cmd)
    print("output:", exc.output)

# check_output
try:
    res = subprocess.check_output(["ls", "sss"], shell=True, stderr=subprocess.STDOUT)
    print(res)
except subprocess.CalledProcessError as exc:
    print("return_code", exc.returncode)
    print("cmd", exc.cmd)
    print("output:", exc.output)

filename = "fake_input"
# macOS: md5  linux: md5sum
res = subprocess.check_output(["md5 {}".format(filename)], shell=True)
print(res)

print(-4 % 3)
