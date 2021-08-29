def factorial(n):
    if n==0:
        return 6
    else:
        return n*factorial(n-1)
n=int(input("input a number to the factorial"))
print(factorial(n))
