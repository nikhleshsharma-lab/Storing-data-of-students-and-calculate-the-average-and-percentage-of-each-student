#Storing data of students and calculate the average and percentage of each student
import math
students=[]
num=int(input("Enter the number of students in the class-"))
subjects=int(input("Enter the number of subjects-"))
for i in range(num):
    name=input("Enter the name-")
    if name.isdigit():
        print("Name cannot be a number")
        name=input("Enter the name-")
    roll_no=int(input("Enter the roll number-"))
    marks = []
    for j in range(subjects):
        mark = int(input(f"Enter marks for subject {j + 1}: "))
        marks.append(mark)
    students.append([name,roll_no,marks])

print("What do you want to print?=")
print("a) Student's Data")
print("b) percentage of student")
print("c) average of student")
choice=input("Enter your choice - ")

if choice=="a":
    for i in students:
        print(i)

elif choice=="b":
    h=input("Enter Student's name-")
    for i in students:
        if i[0]==h:
            total = sum(i[2])
            percentage = (total / (subjects * 100))*100
            print("Persentage scored by",h,"is",percentage,"%")

elif choice=="c":
    y=input("Enter Student's name-")
    for i in students:
        if i[0]==y:
            total = sum(i[2])
            print("Average of",y,"is",(total)/subjects)
else:
    print("Invalid choice")