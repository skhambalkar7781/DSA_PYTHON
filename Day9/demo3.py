class College:
    def college_name(self):
        print("RBU")

class Student(College):
    def student_name(self):
        print("Name : Saurabh")
        print("Branch : MCA[AIML]")
        
class Exam(Student):
    def exam_name(self):
        print("Subject : Python")
        print("Subject2 : Java")
        print("Subject3 : C++")
        
object = Exam()
object.college_name()
object.student_name()
object.exam_name()