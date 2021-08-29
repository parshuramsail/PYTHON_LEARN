# accept string and calculate the upper and lower case letters.
def string_test(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
        print("original string:",s)
        print("no of upper case characters:",d["UPPER_CASE"])
        print("no of lower case characters :",d["LOWER_CASE"])
string_test("the quick brown fox")
