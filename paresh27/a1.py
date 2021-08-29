#PYTHON STATTEMENTS
#1.USE FOR,SPLIT() AND IF STATEMENT THAT WILL PRINT OUT WORDS THAT STARTS WITH "S".
st='print only the words that starts with s in this sentence'
for word in st.split():
    if word[0].lower()=='s':
        print(word)

