class Student:
    school = "Berklee College of Music"

    __slots__ = ("first_name", "last_name", "__neptun_code", "subjects")

    def __init__(self, first_name, last_name, neptun_code, subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.__neptun_code = neptun_code
        self.subjects = subjects

    def __average(self):
        return round(sum(subject["grade"] for subject in self.subjects) / len(self.subjects), 2)

    def credits(self):
        return sum(subject["credit"] for subject in self.subjects if subject["grade"] > 1)

    def log_neptun_code(self):
        print(self.__neptun_code)


if __name__ == "__main__":
    john = Student(
        "John",
        "Doe",
        "ABC123",
        [
            {"subject": "Math", "grade": 1, "credit": 7},
            {"subject": "Physics", "grade": 2, "credit": 4},
            {"subject": "Chemistry", "grade": 3, "credit": 3},
        ],
    )
    print(john.first_name)
    # print(john.__average())
    print(john._Student__average())  # name mangling
    print(john.credits())
    print(john.school)
    print(Student.school)
    Student.school = "New School"
    print(john.school)
    john.log_neptun_code()
    # print(john.__neptun_code)
    print(john._Student__neptun_code)  # name mangling
    # AttributeError: 'Student' object has no attribute 'age' and no __dict__ for setting new
    # student.age = 20
    # print(student.age)
