from company.company import Company
from contract.employment_contract import EmploymentContract
from employees.employee import Employee
from salary_document.salary import Salary

person = Employee("Velmira", "Georgieva", "9408303257", "Sofia, Bulgaria")
contract = EmploymentContract("12-09-2023", 8, "developer", 2500.00)
contract.appoint_employee(person)
company = Company("XYZ", "1111111111", "Sofia", 1234, "Mira M")
company.add_contract(contract)
fish = Salary(company, "august", 20)
fish.calculate_net_salary_employeecontract()