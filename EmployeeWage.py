import random


class EmployeeWageComputation:
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    HALF_DAY_HOUR = 4

    def check_attendance(self):
        random_attendance = round(random.randint(0, 2))
        if random_attendance == 1:
            print("Employee is working full day")
            return self.FULL_DAY_HOUR
        if random_attendance == 2:
            print("Employee is working part time")
            return self.HALF_DAY_HOUR
        print("Employee is absent")
        return 0

    def calculate_daily_wage(self, hours):
        return hours * self.WAGE_PER_HOUR
