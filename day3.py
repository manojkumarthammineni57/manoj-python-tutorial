nums=[1,2,3,4,5,]
print(nums)
print(nums[0])
print(nums[1])
print(nums[-1])
print(nums[-4])
print(nums[2:4])
print(nums[2:])
print(nums[:4])

names=['manoj','jagan','vihan']
print(names)

mix=['manoj',65,9.5]
print(mix)

mix=[nums,names]
print(mix)

mix[0]
print(mix)

mix[0]
print(mix[0][0])

len(mix)
print(len(mix))

mix[0][1]
print(mix[1][2])

mix=nums+names
print(mix)

nums.append(20)
print(nums)

nums.insert(1,55)
print(nums)

nums.count(4)
print(nums)
print(4)

nums.remove(4)
print(nums)

nums.pop(2)
print(nums)

del nums[2:4]
print(nums)

nums.extend([9,8,7,6,5,4])
print(nums)

nums[2:4]=[1,3]
print(nums)

nums.reverse()
print(nums)

nums.sort()
print(nums)

min(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
print(min(names))

a=[33,76,24,56]
b=['navin','kiran','harsf']
print((a[:2]+b[1:])[-3])
