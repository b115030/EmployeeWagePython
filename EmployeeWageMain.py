from EmployeeWage import EmployeeWageComputation

employee_wage_computation = EmployeeWageComputation()
no_of_hours = employee_wage_computation.check_attendance()
if no_of_hours:
    print(employee_wage_computation.calculate_daily_wage(no_of_hours))
