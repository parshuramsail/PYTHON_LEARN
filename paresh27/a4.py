#GO THROUGH THE STRING BELOW AND IF THE LENGTH OF A WORD IS EVEN PRINT 'EVEN!'
st='print only the words that starts with s in this sentence'
for word in st.split():
    if len(word)%2==0:
        print(word+ ' is EVEN')

