nums = [2, 5, 8, 3, 1]
print(nums)
print(nums[0])
print(nums[2:])
print(nums[-2])

names = ['devesh', 'vikas', 'sapna']
print(names)
# can have mixed type of list
per = ['string', 64.5, 74]
print(per)

mil = [names, per]
print(mil)

#append add ele to last inedx
nums.append(20)
print(nums)

#insert add ele at a particular index
nums.insert(2, 70)
print(nums)

# remove removes given ele
nums.remove(2)
print(nums)
#pop removes ele wrt to given ele, by default it will remove last ele
nums.pop(0)
print(nums)

#if want to remove multiple ele remove use del
del nums[2:]
print(nums)

#want to add multiple ele use extend
nums.extend([45, 6, 2, 80])
print(nums)
#to get min, max, sum min nums max nums sum nums
x = min (nums)
y = max (nums)
z = sum (nums)
print(x, y, z)

#sort
print(sorted(nums))

