class Student:
    @staticmethod
    def get_personal_detail(first_name, last_name):
        print("Personal Details = ", first_name, last_name)

    @staticmethod
    def contact_detail(mobil_no, rollno):
        print("Contact Details = ", mobil_no, rollno)
        
Student.get_personal_detail("Saurabh", "Khambalkar")
Student.contact_detail(82715152627, 1001)
        