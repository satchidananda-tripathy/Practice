def add(name,age):
    age=age+5
    return name,age

#Example of pass argument by position is, we can not the sequence.
o_nm,o_age=add('satchi',50)
print(o_nm,"was",o_age,"years old before 5 years")

#Let i don't know the sequence of paramiter in the definition. i have to pass by name or name will go as age
o_nm,o_age=add(age=50,name='Ramesh')
print(o_nm,"was",o_age,"years old before 5 years")