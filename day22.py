from array import*
arr1=array("i",[1,2,3,4,5])
arr1.append(8)
for n in arr1:
    print(n)

from array import*
arr1=array("i",[1,2,3,4,56,77])
arr1.reverse()
for n in arr1:
    print(n)

from array import*
arr1=array("i",[1,2,3,4,5,6,7])
arr2=arr1
print(arr1)
print(arr2)

from array import*
arr1=array("i",[1,2,3,4,5,6,7,8])
arr2=arr1
arr1[2]=22
print(arr1)
print(arr2)

from array import*
arr1=array("i",[1,2,3,4,5,6,7,8,9])
arr2=array("i",arr1.tolist())
arr1[4]=54
print(arr1)
print(arr2)