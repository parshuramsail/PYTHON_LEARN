a=10
print(id(a))
b=9
c=11
print(id(a))
def something():
    a=9
    x=globals()['a']
    print(id(x))
    print("inside function",a)
    globals()['a']=15
something()
print("outside function",a)

