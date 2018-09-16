record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print(name, email, phone_numbers)


####


def drop_first_last(grades):
    first, *middle, last = grades
    return myavg(middle)


def myavg(numbers):
    return sum(numbers) / len(numbers)


grades = [12, 4, 6, 9]
print(drop_first_last(grades))

# unpack multi variable
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if 'foo' == tag:
        do_foo(*args)
    if 'bar' == tag:
        do_bar(args)

###
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(":")
print(uname, fields, homedir, sh)
