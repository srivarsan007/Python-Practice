print("----------Student Report----------")

name = input("Enter the student Name :")
regno = input("Enter the student Register number :")
sub1 = int(input("Enter student's mark on 1st Subject :"))
sub2 = int(input("Enter student's mark on 2nd Subject :"))
sub3 = int(input("Enter student's mark on 3rd Subject :"))

Total = sub1+sub2+sub3
print("The Total markes obtained is",Total)
Average = Total/3
print("The Average is",Average)
Percentage = Average
print("The Percentage is",Average,"%")

if Average >= 90 :
    print("Grade is A")
    print("Pass")
elif Average >=75 and Average <=89 :
    print("Grade is B")
    print("Pass")
elif Average >=50 and Average <=74 :
    print("Grade is C")
    print("Pass")
else :
    print("Fail")