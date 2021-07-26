#Let if some one score 0 in a subject, minimum mark will be given to student in a particular subject
def student(name,math=5,eng=6,science=7):
    total_mark=math+eng+science
    return name,total_mark

o_name,tot_score=student('Sachin',10)

print(o_name," has scored ",tot_score)

o_name,tot_score=student('Ramesh',10,80,40)
print(o_name," has scored ",tot_score)

o_name,tot_score=student('Miraj',eng=40)
print(o_name," has scored ",tot_score)