""" 
An employee's total weekly pay equals the hourly wage multiplied by the total number
of regular hours plus any overtime pay. Overtime pay equals the total overtime hours
multiplied by 1.5 times the hourly wage. Write a program that takes as input the
hourly wage, total regular hours, and total overtime hours and displays an employee's
total weekly pay. 
"""

class Employee:
    def __init__(self, hourly_wage, total_regular_hours, total_overtime_hours):
        self.hourly_wage = hourly_wage
        self.total_regular_hours = total_regular_hours
        self.total_overtime_hours = total_overtime_hours
        self.overtime_pay = self.total_overtime_hours * 1.5 * self.hourly_wage  

    def calculate_weekly_pay(self):
        return self.hourly_wage * self.total_regular_hours + self.overtime_pay

if __name__ == '__main__':
    hourly_wage = input("Enter the hourly wage of the employee: ")
    total_regular_hours = input("Enter the total weekly regular hours of the employee: ")
    total_overtime_hours = input("Enter the total weekly overtime hours: ")
    employee = Employee(int(hourly_wage), int(total_regular_hours), int(total_overtime_hours))
    print("The weekly pay of the employee is", employee.calculate_weekly_pay())

