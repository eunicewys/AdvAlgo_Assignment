class Person:
    def __init__(self, name, gender, bio, privacy="public"):
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy.lower()

    def displayProfile(self):
        print("\n------ Profile ------")
        print(f"Name    : {self.name}")
        print(f"Gender  : {self.gender}")
        print(f"Bio     : {self.bio}")
        print(f"Privacy : {self.privacy.capitalize()}")
        print("---------------------")


def addPerson(people_list, person):
    if len(people_list) < 10:
        people_list.append(person)
        print(f"Profile added: {person.name}")
    else:
        print("**Cannot add more profiles. Maximum 10 reached.**")


if __name__ == "__main__":
    people = []

    addPerson(people, Person("Alice", "Female", "Love baking and books", "public"))
    addPerson(people, Person("Bob", "Male", "Tech enthusiast and gamer", "private"))
    addPerson(people, Person("Cara", "Female", "Travelling the world", "public"))
    addPerson(people, Person("Daniel", "Male", "Photography & coffee addict", "public"))
    addPerson(people, Person("Ella", "Female", "Student, reader, dreamer", "private"))
    addPerson(people, Person("Finn", "Male", "Dog dad, engineer", "public"))
    addPerson(people, Person("Gina", "Female", "Cat mom, artist", "private"))
    addPerson(people, Person("Hank", "Male", "Mountain hiker", "public"))
    addPerson(people, Person("Ivy", "Female", "Minimalist lifestyle", "public"))
    addPerson(people, Person("Jake", "Male", "Works in IT", "private"))

    addPerson(people, Person("Kelly", "Female", "Sleeping-beauty", "public"))

    for person in people:
        person.displayProfile()

