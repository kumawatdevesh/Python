x=2
print(x);
x=4
y=3
print(x+y)

#string and number cant be concatanated

name = "devesh"
last = "kumawat"
print(name + last)

print(name[0])
#-1 index start from the last chracter
print(name[-1])
print(name[-3])

print(name[0:3])
# if dont specify ending goes to the end
print(name[1:])

# this will mot work. strins in python are immutable.
#name[0] = 'Y'

# you can do this.
print('my name is ' + name[0:3])
print(len(name))

#address
num = 1
print(num)
print(id(num))

num1 = 2
print(num1)
print(id(num1))
