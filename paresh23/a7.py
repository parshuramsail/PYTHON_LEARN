#python program to reverse a string
def string(str1):
    rstr1=''
    index=len(str1)
    while index > 0:
        rstr1+=str1[index-1]
        index=index-1
    return str1
print(string('12345adsb'))
