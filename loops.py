# while loop

i=1
while i<=5:
    print('devesh ', end="") #to print on same line
    i = i+1

# for loop

tup = [1, 2, 3, 'devesh']

for i in tup:
    print(i, end="")

for i in range(0, 10, 2):
    print(i)


# continue and break
print('break and continue')

x = 6
y = 1
i = int(input("enter num"))

while i> x:
    if(i%3 == 0):
        continue

    
    print(i)
    i = i + 1

while y<=i:
    if(y>i):
        break

    print(y)
    y = y + 1
    

# for else

nums = [2, 3, 4, 5, 6, 7]

for num in nums:
    if(num % 5==0):
        print(num)
        break
else:
    print('nothing happend')





































