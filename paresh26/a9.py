# BREAK,CONTINUE,PASS
#BREAK:BREAKS OUT OF THE CURRENT CLOSET ENCLOSING LOOP.
#CONTINUE:GOES TO THE TOP OF THE CLOSET ENCLOSING LOOP.
#PASS:DOES NOTHING AT ALL.(AVOIDE ERRORS)

#for PASS
#x=[1,2,3]
#for item in x:
#    pass
#print('end of my script')

#for CONTINUE
#mystring='SAMMY'
#for letters in mystring:
#   if letters=='A':
 #       continue
  #  print(letters)

#for BREAK
#mystring='SAMMY'
#for letters in mystring:
 #   if letters=='A':
  #      break
   # print(letters)

x=0
while x<5:
    if x==2:
        break
    print(x)
    x+=1

