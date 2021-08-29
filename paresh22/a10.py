#GIVEN NUMBER COUNT THE TOTAL NUMBER OF DIGITS IN A NUMBER
num=int(input("enter a number:"))
count=0
while num!=0:
    num//=10
    count+=1
print("total digits are:",count)
