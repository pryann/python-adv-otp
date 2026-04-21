from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    first_name: str
    last_name: str
    age: int
    school: str = "Berklee College of Music"

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.age)

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def is_adult(self) -> bool:
        adult_criteria = 18
        return self.age >= adult_criteria


if __name__ == "__main__":
    person = Person(first_name="John", last_name="Doe", age=33)
    person_2 = Person(first_name="jane", last_name="Doe", age=31)
    person_3 = Person(first_name="Johhny", last_name="Doe", age=40)
    print(person.first_name)
    print(person)
    print(person == person_2)
    print(person.full_name())
    print(person.is_adult())
    print(person > person_2)
    people = [person, person_2, person_3]
    print(sorted(people))
    # if frozen is False, we can change the attributes of the object
    # person.hobbies = ["Music", "Reading"]
    # but the repr not changed, becuse the repr is generated at the time of the object creation
    # print(person)
    # but we can ascess the new attribute
    # print(person.hobbies)
