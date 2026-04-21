# class Employee:
#     __slots__ = ("first_name", "last_name", "__salary")

#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.__salary = salary

#     def get_salary(self):
#         return round(self.__salary, 2)

#     def set_salary(self, value):
#         top_salary = 120_000
#         self.__salary = value if value < top_salary else top_salary


class Employee:
    __slots__ = ("first_name", "last_name", "__salary")

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = salary

    @property
    def salary(self):
        return round(self.__salary, 2)

    @salary.setter
    def salary(self, value):
        top_salary = 120_000
        self.__salary = value if value < top_salary else top_salary

    @salary.deleter
    def salary(self):
        print("Person is fired")
        del self.__salary


if __name__ == "__main__":
    person = Employee("John", "Doe", 100_000)
    print(person.salary)
    person.salary = 150_000
    print(person.salary)
    del person.salary
    # AttributeError: 'Employee' object has no attribute '_Employee__salary'
    print(person.salary)

    # print(person.get_salary())
    # person.set_salary(150_000)
    # print(person.get_salary())
