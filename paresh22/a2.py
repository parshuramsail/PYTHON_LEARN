#WHILE WITH ELSE
a=1
while a<=3:
    b=int(input("enter a number:"))
    if b==0:
        print("exiting loop with with loop with break command,else is not executed")
        break
    a+=1
else:
    print("loop exited withoutt executig break command")


