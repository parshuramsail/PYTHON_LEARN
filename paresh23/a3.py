x=(input("enter a number:"))
y=(input("enter a number:"))
z=(input("enter a number:"))
def max1(x,y,z):
    if (x>y) and (x>z):
        return x
    elif (y>x) and (y>z):
        return y
    else:
        return z
#def max2(x,y,z):
    return max1(x,y,z)
print(max1(x,y,z))
