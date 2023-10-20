from company.company import Company


class Salary:
    def __init__(self, company: Company, month: str, work_days: int):
        self.company = company
        self.month = month
        self.work_days = work_days  # It can be connected according to the month to take the number of working days

    def employees(self):
        employees = []
        employees = self.company.contracts
        return employees

    def calculate_net_salary_employeecontract(self):
        employees = self.company.contracts
        for key, value in employees.items():
            if key == "employmentContract":
                if value is None:
                    raise ValueError("There are no employees assigned to the company")

                for p in value:
                    person = p.employee.first_name + " " + p.employee.last_name
                    sal_gross = p.salary
                    DOO = 0.0838 * sal_gross
                    DZPO = 0.022 * sal_gross
                    ZO = 0.032 * sal_gross
                    DOD = (sal_gross - (DOO + DZPO + ZO)) * 0.1
                    net_sal = sal_gross - (DOO + DZPO + ZO + DOD)
                    print(f"За служител {person} с брутна заплата {sal_gross} "
                          f"са начислени следните осигуровки \n"
                          f"ДОД : {DOD}, ДЗПО: {DZPO}, ЗО : {ZO}, ДОД : {DOO} \n"
                          f"Размера на натната заплата е {net_sal}")

    def add_pay_vacantion(self,name, day):
        employees = self.employees()
        for key, value in employees.items():
            if key == "employmentContract":
                if value is None:
                    raise ValueError("There are no employees assigned to the company")

            for p in value:
                check = p.employee.vacantion + day
                if check >= p.employee.vacantion:
                    Exception("The employee has reached the maximum allowed leave under this contract")

                days_left = p.vacantion - p.employee.vacantion
                if days_left > day:
                    Exception(f"The employee has {days_left} days left")
                p.employee.vacantion += day
                p.employee.additional_status = "leave"
                self.work_days -= day
        return "The holiday is reflected in the calculation of the salary"


    def add_nonpayvacantion(self, day):
        employees = self.employees()
        for key, value in employees.items():
            if key == "employmentContract":
                if value is None:
                    raise ValueError("There are no employees assigned to the company")
        self.employee.vacantion += day
        self.employee.additional_status = "leave"
        self.month_work_day -= day
        return "The holiday is reflected in the calculation of the salary"
