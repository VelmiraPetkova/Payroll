from contract.base_contract import Contract
from contract.employment_contract import EmploymentContract


class Company:
    def __init__(self, name: str, company_id: str, address: str, economic_activities: int, manager: str):
        self.name = name
        self.company_id = company_id
        self.address = address
        self.economic_activities = economic_activities
        self.manager = manager
        self.contracts = {"employmentContract": []}  # List of number of contract To DO

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isspace() or value == "":
            raise ValueError("The company name is not allowed to be empty!")
        self.__name = value

    @property
    def company_id(self):
        return self.__company_id

    @company_id.setter
    def company_id(self, value):
        if len(value) < 10 or value.isalpha():
            raise ValueError("Company ID should be 10 symbols long!")
        self.__company_id = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if value.isspace() or value == "":
            raise ValueError("The company address is not allowed to be empty!")
        self.__address = value

    def add_contract(self, contract: Contract):
        if contract.employee is None:
            raise ValueError("The contract has no appointed employee")

        if isinstance(contract, EmploymentContract):
            self.contracts["employmentContract"].append(contract)

    def remuve_contract(self, contract):
        if contract.employee is None:
            raise ValueError("The contract has no appointed employee")
        if contract.employee.status == "unappointed":
            for key, value in self.contracts.items():
                if isinstance(contract, EmploymentContract) and key == "employmentContract":
                    value.remove(contract)
