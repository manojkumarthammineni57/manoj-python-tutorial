a=5
b=5
id(a)
id(b)
print(a)
print(b)
print(id(a))
print(id(b))
b=6
print(id(b))

name='manoj'
name1='manoj'
print(id(name))
print(id(name1))

name='my fav color is red'
name1='my fav color is red'
print(id(name))
print(id(name1))

a=1000
b=2000
print(id(a))
print(id(b)) 

k=2000
print(id(k))

a='telusuko'
b='telusuko'
print(id(a)==id(b))