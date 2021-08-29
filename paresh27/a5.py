#write a program that prints the integers from 1 to 100.but for multipkes of three print "fizz" instead of numbers .
#and for the mutiples of five print"buzz".for numbers which are multiples of both three and five print'fizzbuzz'
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FIZZBUZZ")
    elif i %3==0:
        print("FIZZ")
    elif i % 5==0:
        print('BUZZ')
    else:
        print(i)
