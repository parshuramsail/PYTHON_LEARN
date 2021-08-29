#write a program to sum all the number in a list
def sum(numbers):
    total=0
    for x in numbers:
        total+=x
    return total
print(sum((1,2,3,4,5,6,7,8,9)))
