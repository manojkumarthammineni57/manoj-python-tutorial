def add(num1,num2):
    return num1+num2
result=add(4,5)
print(result)

def add(num1,num2=0):
    return num1+num2
result=add(4)
print(result)

def add(num1=0,num2=0):
    return num1+num2
result=add(4)
print(result)

def add(num1=0,num2=0):
    return num1+num2
result=add(4,5)
print(result)

def add(num1,*num2):
    print(num1)
    print(num2)
    return 0
result=add(4,5,6,7)
print(result)

def add(num1,*num2):
 sum=num1
 for n in num2:
     sum+=n
     return sum
 result=add(4,5,6,7)
 print(result)

 def person(name,age):
     print("name:",name)
     print("age:",age)
 person("manoj",21)
 print(person)

 def person(name,age=20):
     print("name:",name)
     print("age:",age)
 person("manoj") 
 print(person)

 def person(name,age):
     print("name:",name)
     print("age:",age)
 person(age=20,name="manoj")
 print(person)

 def person(name,**kwlargs):
     print("name:",name)
     for k,v in kwlargs.items():
         print(k,":",v)
         person(name="manoj",age=20,loc="gdp",tech="python")
         print(person) 


     

