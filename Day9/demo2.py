class College:
    def college_name(self):
        print("RBU")

class Student(College):
    def student_name(self):
        print("Name : Saurabh")
        print("Branch : MCA[AIML]")
        
object = Student()
object.college_name()
object.student_name()