#write a program which takes two digits m(row) and n (coloumn) as input and genertes a two dimensionalarray
#the element value in the ith row and jth coloumn of the array should be i*j
#note:i=0,1....,m-1
#    j=0,1,n-1
row_num=int(input("input number of rows:"))
col_num=int(input("input number of rows:"))
multi_list=[[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]=row*col
print(multi_list)
