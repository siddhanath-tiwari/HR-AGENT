# phase 4.4

import pandas as pd

class PayrollManager:
    def __init__(self, payroll_file="database/payroll/payroll_data.xlsx"):
        self.payroll_file = payroll_file
        self.df = pd.read_excel(self.payroll_file)

    def calculate_salary(self, employee_id):
        """Calculates final salary after leave deductions."""
        employee_data = self.df[self.df["Employee_ID"] == employee_id]
        if employee_data.empty:
            return "Employee not found!"
        
        salary = employee_data.iloc[0]["Base_Salary"]
        leaves = employee_data.iloc[0]["Leaves_Taken"]
        leave_deduction = (salary / 30) * leaves  # 30 days in a month
        final_salary = salary - leave_deduction

        return {"Employee_ID": employee_id, "Final_Salary": final_salary}