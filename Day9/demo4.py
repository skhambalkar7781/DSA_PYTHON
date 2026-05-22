class Rbi:
    def home_loan(self):
        print("Home loan ROI = 8%")
        
    def education_loan(self):
        print("Education loan ROI = 7%")
        
class Sbi(Rbi):
    def home_loan(self):
        print("Home loan ROI = 10%")
        super().education_loan()
        
obj = Sbi()
# obj.home_loan()
obj.education_loan()