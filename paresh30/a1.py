#LESSER OF TWO EVENS:write a function that returns the lesser of two given numbers.if both numbers are even ,returns greater if one or both numbers are odd.
#lesser_of_two_evens(2,4)----2
#lesser
def lesser_of_two_even(a,b):
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
    return result
lesser_of_two_even(2,4)

