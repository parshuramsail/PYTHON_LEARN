#write a program to sum of all the numbers in a list
def sum(numbers):
    total=0
    for x in numbers:
        total+=x
    return total
print(sum((8,2,3,0,7)))
