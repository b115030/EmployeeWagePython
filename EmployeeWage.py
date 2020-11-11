import random
def print_welcome():
    print("Welcome to Employee Wage Computation Problem")
    return True
def check_attendance():
    random_attendance = round(random.random())
    if random_attendance == 1:
        print("Employee is present")
        return True
    print("Employee is absent")
    return False