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