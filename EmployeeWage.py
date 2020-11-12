import random


class EmployeeWageComputation:
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    HALF_DAY_HOUR = 4
    WORKING_DAYS_FOR_MONTH = 20

    def full_time(self):
        print(f'Employee is working full day. Wage for the day is: {self.calculate_daily_wage(self.FULL_DAY_HOUR)}')
        return self.calculate_daily_wage(self.FULL_DAY_HOUR)

    def part_time(self):
        print(f'Employee is working half day. Wage for the day is: {self.calculate_daily_wage(self.HALF_DAY_HOUR)}')
        return self.calculate_daily_wage(self.HALF_DAY_HOUR)

    def absent(self):
        print("Employee is absent for the day")
        return 0

    def calculate_daily_wage(self, hours):
        return hours * self.WAGE_PER_HOUR

    def check_attendance(self):
        random_attendance = round(random.randint(0, 2))
        return {
            0: self.full_time(),
            1: self.part_time()
        }.get(random_attendance, self.absent())

    def calculate_monthly_wage(self):
        monthly_wage = 0
        for days in range(self.WORKING_DAYS_FOR_MONTH):
            print("For day ", days+1)
            monthly_wage += self.check_attendance()
        print(f'Total monthly wage is {monthly_wage}')