#def person(name,**data):
 #   print(name)
  #  print(data)
#person(name="ram",age=20,mob=6585746)

def person(name,**data):
    print("name",name)
    for i,j in data.items():
        print(i,j)
person(name="ram",age=20,mob=6585746)
