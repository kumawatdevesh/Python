def hello():
    print('hello world')

hello()

def add(a, b):
    c = a+b
    print(c)

add(2, 3)

# return a value

def add(a, b):
    c = a+b
    return c

val = add(10, 3)
print(val)

def sub(a, b):
    c = a+b
    d = a-b
    return c, d

val1, val2 = sub(5, 3)
print(val1)
print(val2)

def args(name, *data):
    print(name)
    print(data)

args('devesh', 23, 45, 5)

def kwargs(name, **data):
    print(name)
    print(data)

kwargs('devesh',first=23,second='vikas',third='sapna')

a=10 #global variable

def value():
    a=1777
    print(a)

value()
print(a)

# recursion

def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)

ans = fact(7)
print(ans)

# lambda function

l = lambda a: a*a

val = l(10)
print(val)
    
