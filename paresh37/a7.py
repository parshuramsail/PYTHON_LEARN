#program that accept a word from the user & reverse it.
word =input("enter a word to reverse")
for char in range(len(word)-1,-1,-1):
    print(word[char],end='')
print("\n")
