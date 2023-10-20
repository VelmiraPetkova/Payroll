class Employee:
    STATUS_PERMITTED = ["unappointed", "appointed"]
    ADD_STATUS_PERMITTED = ["no work", "work", "sick", "leave"]

    def __init__(self, first_name, last_name, employee_id, address, work_experience=0):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.address = address
        self.status = "unappointed"
        self.additional_status = "no work"
        self.vacantion = 0
        self.working_hours = 12
        self.work_experience = work_experience

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value.isspace() or value == "":
            raise ValueError("Worker name cannot be empty!")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value.isspace() or value == "":
            raise ValueError("Worker name cannot be empty!")
        self.__last_name = value

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        if len(value) < 10:
            raise ValueError("Client ID should be 10 symbols long!")
        self.__employee_id = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if value.isspace() or value == "" or len(value) < 3:
            raise ValueError("Entered the employee's address")
        self.__address = value

    def change_address(self, new_address):
        self.address = new_address
        return f"{self.first_name} {self.last_name} has a new address."

    def change_last_name(self, new_name):
        old_name = self.last_name
        self.last_name = new_name
        return f"The name was change from {old_name} to {new_name}"

    def change_status(self):
        self.status = "appointed"
        self.additional_status = "work"

    def change_work_experience(self):
        self.work_experience += 1