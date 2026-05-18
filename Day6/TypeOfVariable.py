# class new:
#     def __init__(self):
#         self.a = 10
        
# obj1 = new()
# obj2 = new()
# obj3 = new()
# obj1.a = 20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# ==========================================================

# class new:
#     a  =10
#     def __init__(self):
#         self.name="Saurabh"

# obj1 = new()
# obj2 = new()
# obj3 = new()
# new.a = 50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# ==============================================================
class college:
    collegename = "modern college"
    def __init__(self):
        self.studentname = "saurabh"

principal = college()
teacher = college()
student = college()
print(principal.collegename)
print(teacher.collegename)
print(student.collegename)
college.collegename = "HBD"  #//sattic variable
principal.studentname="Saurabhkhambalkar" #//instance variable
print(principal.studentname,"   ",principal.collegename)
print(teacher.studentname, " ",teacher.collegename)
print(student.studentname, " ",student.collegename)


