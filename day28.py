def square(num):
    return num*num
def cube(num):
    return num*num*num
value=5
result=square(5)
print(result)

def square(num):
    return num*num
def cube(num):
    return num*num*num
value=8
result=cube(8)
print(result)

def square(num):
    return num*num
def cube(num):
    return num*num*num
def operate(num,operate):
    return operate(num)
value=5
result=operate(value,cube)
print(result)  


def square(num):
    return num*num
def cube(num):
    return num*num*num
def operate(num,operate):
    for i in num:
        result=operate(i)
        print(result)
nums=[5,6,7]
operate(nums,cube)
        

    