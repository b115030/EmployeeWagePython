import csv
import random
from company import Companies


class EmployeeWageComputation:
    '''
            A Class to represent Employee
            ...
            Attributes
            ----------
                WAGE_PER_HOUR : int
                            Wage per hour for an employee
                FULL_DAY_HOUR : int
                            Total working hours in a day for full time employee
                HALF_DAY_HOUR : int
                            Total working hours for part time
                MAX_DAYS : int
                        Maximum no. of working days in a month
                MAX_HOURS : int
                        Maximum no. of working hours in a month

            Methods
            -------
                full_time(self)
                        :returns
                            daily wage for a full time employee
                part_time(self)
                        :returns
                            daily wage for a part time employee
                absent(self)
                        :returns
                            0
                calculate_daily_wage(self, hours)
                        :returns
                            wage of the employee for the day
                check_attendance(self)
                        :returns
                            wage after checking attendance of the employee
                calculate_wage_till_total_hour_or_days(self)
                        :returns
                            total_wage after reaching the limiting condition
                calculate_monthly_wage(self)
                        :returns
                            monthly_wage after checking attendace
            '''
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    HALF_DAY_HOUR = 4
    WORKING_DAYS_FOR_MONTH = 20
    MAX_DAYS = 20
    MAX_HOURS = 100
    company_list = []

    def full_time(self):
        """
                        calculates daily wage for full time employee
                        :parameter:
                                    self
                        :return:
                                    calculate_daily_wage(FULL_DAY_HOUR)
                """
        print(f'Employee is working full day. Wage for the day is: {self.calculate_daily_wage(self.FULL_DAY_HOUR)}')
        return self.calculate_daily_wage(self.FULL_DAY_HOUR)

    def part_time(self):
        """
                        calculates daily wage for part time employee
                        :parameter:
                                    self
                        :return:
                                    calculate_daily_wage(HALF_DAY_HOUR)
                """
        print(f'Employee is working half day. Wage for the day is: {self.calculate_daily_wage(self.HALF_DAY_HOUR)}')
        return self.calculate_daily_wage(self.HALF_DAY_HOUR)

    def absent(self):
        print("Employee is absent for the day")
        return 0

    def calculate_daily_wage(self, hours):
        return hours * self.WAGE_PER_HOUR

    def check_attendance(self):
        """
                        checks attendance and returns daily wage accordingly
                        :parameter:
                                    self
                        :return:
                                    daily_wage_func() (dictionary) : dictionary of functional calls
                """
        random_attendance = round(random.randint(0, 2))
        daily_wage_func = {
            0: self.full_time,
            1: self.part_time
        }.get(random_attendance, self.absent)
        return daily_wage_func()

    def calculate_wage_till_total_hour_or_days(self):
        """
                        checks attendance and returns total wage accordingly until limiting condition is reached
                        :parameter:
                                    self
                        :return:
                                    total_wage (int)
                """
        hours = 100
        days = self.WORKING_DAYS_FOR_MONTH
        total_wage = 0
        while hours > 0 and days > 0:
            wage = self.check_attendance()
            total_wage += wage
            if wage == self.calculate_daily_wage(self.FULL_DAY_HOUR):
                hours -= self.FULL_DAY_HOUR
            elif wage == self.calculate_daily_wage(self.HALF_DAY_HOUR):
                hours -= self.HALF_DAY_HOUR
            else:
                pass
            days -= 1
        return total_wage

    def calculate_monthly_wage(self):
        """
                        calculates monthly wage
                        :parameter:
                                    self
                """
        monthly_wage = 0
        for days in range(self.WORKING_DAYS_FOR_MONTH):
            print("For day ", days + 1)
            monthly_wage += self.check_attendance()
        print(f'Total monthly wage is {monthly_wage}')

    def add_company(self, company_name, wage_per_hour, full_day_hour, working_days_for_month, total_working_days):
        """
                        calculates monthly wage
                        :parameter:
                                    self
                """
        self.company_list.append(
            Companies(company_name, wage_per_hour, full_day_hour, working_days_for_month, total_working_days))

    def total_daily_wage_computation(self, company_name):
        if len(self.company_list) == 0:
            print("no companies registered")
            return False
        for company in self.company_list:
            print(company)


