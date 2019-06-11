num = 2.3
print(type(num))

num1 = 2
print(type(num1))

num2 = 2+3j
print(type(num2))

#convert from one data type from another
print(int(num))
print(float(num1))
print(complex(num2, num1))

print(num > num1)

bool = num > num1
print(type(bool))

# true give 1 and flase gives 0
print(int(bool))

list = [1, 2, 3, 4, 5, 6]
print(type(list))

s = {1, 2, 3, 4, 5, 6}
print(type(s))

tup = (1, 2, 3, 4, 5, 6)
print(type(tup))

string = "devesh"
print(type(string))

# specify the range you want number in
rangee = range(1, 10)
tupl = tuple(rangee)
print(tupl)

rangee1 = range(1, 10, 2) # print number till 10 with diff of 2
tupl1 = tuple(rangee1)
print(tupl1)

# dictonaries

d = {"devesh": "under", "vikas": "ca", "sapna": "masters"}
print(d.keys())
print(d.values())
print(d['devesh'])
print(d.get('devesh'))




