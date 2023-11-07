class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_name = person["name"]

        if person.get("wife"):
            Person.people[person_name].wife = Person.people[person["wife"]]

        if person.get("husband"):
            Person.people[person_name].husband = (
                Person.people)[person["husband"]]

    return result
