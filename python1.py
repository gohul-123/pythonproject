name = input("enter the student name : ")
n=int(input("enter the number of subjects : "))
total = 0
for i in range(1,n+1):
    mark = float(input(f"enter the mark for the subjects{i} : "))
    total = mark 
percentage = total/n
if percentage >=90:
    grade = "A+"
    performance = "Outstanding"
elif percentage >=80 : 
    grade = "A"
    performance = "excellent"
elif percentage >=70 : 
    grade = "B"
    performance = "very Good "
elif percentage >=60 : 
    grade = "c"
    performance = "Good"
elif percentage >=50 : 
    grade = "o"
    performance ="average"
else : 
    grade = "f"
    performance = "need improvement"

print("\n------Academic performance--------")
print("student name :",name)
print("total mark : ",mark )
print("percentage : ",round(percentage,2),"%")
print("grade : ",grade)
print("performance",performance )