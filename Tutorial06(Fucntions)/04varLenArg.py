def person(**data):
    print(data)
    for i,j in data.items():
        print(i,":",j)

person(name="Suraj", age=22, city="Mumbai", contact=9087654321)
