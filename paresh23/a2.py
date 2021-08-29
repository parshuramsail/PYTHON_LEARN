#write a program to find the largest among the two numbers.
x=(input("enter a number:"))
y=(input("enter a number:"))
z=(input("enter a number:"))
def max1(x,y):
    if x>y:
        return x
    return y
def max2(x,y,z):
    return max1(x,max1(y,z))
print(max2(x,y,z))
