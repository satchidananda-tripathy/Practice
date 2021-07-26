def person(id,**data):
    print(id,end=" ")
    for i,j in data.items():
            print(i,j)


person(1,name='Sachin',city='bmpur',age=35,phone=9861594290)
person(2,name='Babu',city='sonepur',age=36,phone=9861183456)
person(2,name='Sunil',city='Binka',phone=9761183456,age=37)