a=10
def something():
    print(globals()['a'])
    a=15
    print("inside:",a)
    something()
    print("outside:",a)

a=10
