import logging
# from typing import Any


class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """
        The __str__ method is used to define the string representation of an object.
        It is called when you use the str() function or when you print the object.
        The __str__ method should return a human-readable string that represents the object.
        """
        return f"({self.first_name},{self.last_name},{self.age})"

    def __repr__(self):
        """
        The __repr__ method is used to define the official string representation of an object.
        It is called when you use the repr() function or when you inspect the object in a REPL.
        The __repr__ method should return a string that, if possible, can be used to recreate the object.
        If the __str__ method is not defined, the __repr__ method will be used as a fallback for the str() function and print() function.
        """
        return f"{self.__class__.__name__}(first_name={self.first_name}, last_name={self.last_name}, age={self.age})"

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif not isinstance(other, Person):
            return False
        else:
            # fmt: off
            # we not check the other attributes
            return (
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.age == other.age
            )


if __name__ == "__main__":
    person = Person("John", "Doe", 33)
    print(person)
    print(str(person))  # it will use __str__ method
    print(repr(person))
    logging.warning(person)  # it will use __str__, if you use r" string it will use __repr__
    person_2 = Person("Jane", "Doe", 33)
    print(person == person_2)
