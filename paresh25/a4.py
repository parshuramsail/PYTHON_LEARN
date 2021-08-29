#WRITE A PROGRAM THAT PRINTS ALL THE NMBERS FROM 0 TO 6 EXCEPT 3 AND 6
for x in range(6):
    if (x==3 or x==6):
        continue
    print(x)
print("\n")
