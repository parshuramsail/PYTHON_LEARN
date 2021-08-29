def update(x):
    print(id(x))
    x[1]=25
    print(id(x))
    print("x",x)
x=[10,20,30]
print(id(x))
update(x)
print("a",x)
