#find our if the word "DOG" is in a string?
def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False
dog_check('my dog ran away')

