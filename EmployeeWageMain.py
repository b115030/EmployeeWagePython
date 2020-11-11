from EmployeeWage import EmployeeWageComputation
employee_wage_computation = EmployeeWageComputation()
if employee_wage_computation.check_attendance():
    print(employee_wage_computation.calculate_daily_wage())