def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person("navin",age=20,loc="mumbai",mob=64873689)
