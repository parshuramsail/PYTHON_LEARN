# WRITE A PROGRAM WHICH ITERATES THE INTEGERS FROM 1 TO 50.
# FOR MULTIPLESNOF THREE PRINT "Fizz"INSTEAD OF THE NUMBERS WHICH ARE MULTIPLES OF BOTH THREE AND FIVE PRINT""FizzBuzz
for fizzbuzz in range(51):
    if fizzbuzz%3==0 and fizzbuzz%5==0:
        print("FIZZBUZZ")
        continue
    elif fizzbuzz%3==0:
        print('FIZZ')
        continue
    elif fizzbuzz%5==0:
        print("BUZZ")
        continue
    print(fizzbuzz)

