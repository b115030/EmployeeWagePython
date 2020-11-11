import random

class EmployeeWageComputation:
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    HALF_DAY_HOUR = 4

    def check_attendance(self):
        random_attendance = round(random.randint(0, 2))
        switcher = {
            1: "Employee is working full day. Wage for the day is: {}".format(self.calculate_daily_wage(self.FULL_DAY_HOUR)),
            2: "Employee is working half day. Wage for the day is: {}".format(self.calculate_daily_wage(self.HALF_DAY_HOUR)),
            0: "Employee is absent"
        }
        return switcher.get(random_attendance, "Invalid Choice")

    def calculate_daily_wage(self, hours):
        return hours * self.WAGE_PER_HOUR
