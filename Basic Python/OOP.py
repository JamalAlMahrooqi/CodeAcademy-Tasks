class Employee:
    
    def __init__(self,emp_name,emp_id,emp_salary,emp_department,hours_worked):
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        self.hours_worked=hours_worked
        self.emp_id=emp_id
    

    def assign_department(self,a_dep):
        self.emp_department=a_dep
        
    def print_employee_details(self):
        return f"Name: {self.emp_name} ID: {self.emp_id} Department: {self.emp_department} Salary: {self.emp_salary} Hours worked: {self.hours_worked}"

    def calculate_emp_salary(self,hw):
        if hw > 50 :
            overtime=hw -50
            overtime_amount=(overtime*(self.emp_salary/50))
            overall_salary= overtime_amount + self.emp_salary
            return overall_salary


e1= Employee("ADAMS", "E7876", 500, "ACCOUNTING",50)
print(e1.print_employee_details())
print(e1.calculate_emp_salary(60))
