class Person:
    def __init__(self, name, gender, bio, privacy="public"):
        """
        Create a new Person with basic social media profile information.
        """
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy.lower()  # 'public' or 'private'

    def displayProfile(self):
        """
        Show the person's profile info.
        """
        print("------ Profile ------")
        print(f"Name    : {self.name}")
        print(f"Gender  : {self.gender}")
        print(f"Bio     : {self.bio}")
        print(f"Privacy : {self.privacy.capitalize()}")
        print("---------------------")


# -------------------------------
# Create and display 5 profiles
# -------------------------------
if __name__ == "__main__":
    # Creating 5 Person objects
    person1 = Person("Alice", "Female", "Love baking and books", "public")
    person2 = Person("Bob", "Male", "Tech enthusiast and gamer", "private")
    person3 = Person("Cara", "Female", "Travelling the world", "public")
    person4 = Person("Dan", "Male", "Photography & coffee addict", "public")
    person5 = Person("Ella", "Female", "Student, reader, dreamer", "private")

    # List of all people
    people = [person1, person2, person3, person4, person5]

    # Display each profile
    for person in people:
        person.displayProfile()
