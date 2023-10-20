#import datetime

from contract.base_contract import Contract
from employees.employee import Employee


class EmploymentContract(Contract):
    def __init__(self, date: str, working_hours: int, position: str, salary: float):
        super().__init__(date, working_hours)
        self.position = position
        self.salary = salary
        self.vacantion = 20

   # @property
    #def date(self):
    #    return self.__date

    #@date.setter
    #def date(self, value):
    #    d = value[0:1]
    #    m = value[2:5]
    #    y = value[5:]
     #   x = datetime.datetime(y, m, d)  # (2018, 6, 1)
    #    self.__date = x.strftime("%x")

    @property
    def working_hours(self):
        return self.__working_hours

    @working_hours.setter
    def working_hours(self, value):
        if value > 8:
            raise Exception("The employee cannot work more than 8 hours under this contract!")
        self.__working_hours = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 710:
            raise ValueError("Salary is smaller than permition")
        self.__salary = value

    def appoint_employee(self, worker: Employee):
        if self.employee is not None:
            ValueError("The employee cannot be added!")

        if worker.working_hours <= 0 or worker.working_hours < self.__working_hours:
            raise Exception("The employee works a maximum number of hours!")

        self.employee = worker
        worker.working_hours -= self.__working_hours
        worker.change_status()
        return f"{worker.first_name} {worker.last_name} was appointed"

    def fired_employee(self, worker):
        if self.employee is None:
            ValueError("The employee is not appointed under this contract!")
        self.employee = None
        worker.working_hours += self.__working_hours
        worker.status = "unappointed"
        worker.additional_status = "no work"
        return f"{worker.first_name} {worker.last_name} was dismissed"

    def change_position(self, new_position):
        old_position = self.position
        self.position = new_position
        return f"The position was change from {old_position} to {new_position}"

    def change_salary(self, new_salary):
        # if new_salary < self.salary:
        #    ValueError("The salary you enter is lower than the current one.")
        self.salary = new_salary
        return "The salary was change"
