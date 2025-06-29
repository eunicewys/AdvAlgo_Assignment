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



if __name__ == "__main__":
    person1 = Person("Alice", "Female", "Love baking and books", "public")
    person2 = Person("Bob", "Male", "Tech enthusiast and gamer", "private")
    person3 = Person("Cara", "Female", "Travelling the world", "public")
    person4 = Person("Dan", "Male", "Photography & coffee addict", "public")
    person5 = Person("Ella", "Female", "Student, reader, dreamer", "private")

    people = [person1, person2, person3, person4, person5]

    for person in people:
        person.displayProfile()
