class Address:
    pc = {"Благоевград": 2700, "Бургас": 8000, "Варна": 9000, "Велико Търново": 5000, "Видин": 3700, "Враца": 3000,
          "Габрово": 5300, "Добрич": 9300, "Кърджали": 6600, "Кюстендил": 2500, "Ловеч": 5500, "Монтана": 3400,
          "Пазарджик": 4400,
          "Перник": 2300, "Плевен": 5800, "Пловдив": 4000, "Разград": 7200, "София": 1000
          }

    def __init__(self, city: str,  street: str = None, boulevard: str = None, number: int = None):
        self.country = "България"
        self.city = city
        self.postal_code = Address.pc[city]
        self.street = street
        self.boulevard = boulevard
        self.number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if value.isspace() or value == "" or value not in Address.pc:
            raise ValueError("Града е задължителен атрибут на адреса!")
        self.__city = value

    @property
    def getAddres(self):
        return self.city


    def __repr__(self):
        res = "Текущият адрес е:\n"
        res += f"{self.country}, Град: {self.city} с ПК:{self.postal_code} "
        if self.street is not None:
            res += f"{self.street}\n"
        if self.boulevard is not None:
            res += f"{self.boulevard}\n"
        if self.number is not None:
            res += f"{self.number}"

        return res


#a = Address("Монтана", "Младост")
#print(a)





    def add_sick(self, sick_day):
        if self.employee is None:
            Exception("There is no assigned contract officer.")
        if self.employee.work_experience < 6:
            ValueError("The employee does not have the necessary months in insurance")
        self.employee.additional_status = "sick"
        self.month_work_day -= (sick_day - 3)