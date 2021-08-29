def two_even(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            result=a
        else:
            result=b
    else:
        if a>b:
            result=a
        else:
            result=b
    return(result)
bb=two_even(2,4)
print(bb)
