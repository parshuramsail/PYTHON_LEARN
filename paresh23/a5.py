#MULTIFLY ALL NUMBERS IN A LIST
def multiply(numbers):
    total=1
    for x in numbers:
        total*=x
    return total
print(multiply((1,2,2,2,2)))
