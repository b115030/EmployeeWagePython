import random
class EmployeeWageComputation:
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    def check_attendance(self):
        random_attendance = round(random.random())
        if random_attendance == 1:
            print("Employee is present")
            return True
        print("Employee is absent")
        return False
    def calculate_daily_wage(self):
        return self.WAGE_PER_HOUR*self.FULL_DAY_HOUR
