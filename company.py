class Companies:
    def __init__(self, COMPANY_NAME, WAGE_PER_HOUR, FULL_DAY_HOUR, MONTHLY_WORKING_DAY, TOTAL_WORKING_HOURS):
        self.WAGE_PER_HOUR = WAGE_PER_HOUR,
        self.FULL_DAY_HOUR = FULL_DAY_HOUR,
        self.MONTHLY_WORKING_DAY = MONTHLY_WORKING_DAY,
        self.TOTAL_WORKING_HOURS = TOTAL_WORKING_HOURS,
        self.COMPANY_NAME = COMPANY_NAME

    def get_company_name(self):
        return self.COMPANY_NAME
    def get_wage_per_hour(self):
        return self.WAGE_PER_HOUR