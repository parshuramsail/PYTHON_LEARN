def count (list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
list=[20,15,12,14,16,17,19,11,13,15,17,19]
even,odd=count(list)
print(even)
print(odd)
