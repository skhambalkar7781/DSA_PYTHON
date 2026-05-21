# import csv
# f = open("employee.csv",'a')
# a = csv.writer(f)
# # a.writerow(["EmpId","Emp Name","Emp Age"])
# empid = int(input("Enter the empid: "))
# empname = input("Enter the empname: ")
# empage = int(input("Enter the empage: "))
# a.writerow([empid,empname,empage])
# print("file is created")

# =========================================================

import csv 
f = open("student.csv",'a')
x = csv.writer(f)
x.writerow(["studentId","StudentName","phy","chem","maths","Total","Percentage","Result"])
# studentId = int(input("Enter the studentId: "))
# StudentName = input("Enter the StudentName: ")
# phy = int(input("Enter the phy: "))
# chem = int(input("Enter the chem: "))
# maths = int(input("Enter the maths: "))
# Total = phy+chem+maths
# Percentage = Total/3
# if Percentage >= 40:
#     Result = "Pass"
# else:
#     Result = "Fail"
# a.writerow([studentId,StudentName,phy,chem,maths,Total,Percentage,Result])
print("file is created")