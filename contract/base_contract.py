from abc import ABC, abstractmethod


class Contract(ABC):
    NUBER_CONTRACT = 0

    def __init__(self, date: str, working_hours: int):
        Contract.NUBER_CONTRACT += 1
        self.date = date
        self.number = Contract.NUBER_CONTRACT
        self.working_hours = working_hours
        self.employee = None  # obeject of type employ

    @abstractmethod
    def appoint_employee(self, worker):
        # To change the status of the employee. Any change of status must be reflected in the other classes as well.
        pass

    @abstractmethod
    def fired_employee(self, worker):
        pass
