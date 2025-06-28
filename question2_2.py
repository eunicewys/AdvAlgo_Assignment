class Person:
    def __init__(self, name, gender, bio, privacy="public"):
        """
        Create a new Person with basic social media profile information.
        """
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy.lower()

    def display_profile(self):
        print("\n------ Profile ------")
        print(f"Name    : {self.name}")
        print(f"Gender  : {self.gender}")
        print(f"Bio     : {self.bio}")
        print(f"Privacy : {self.privacy.capitalize()}")
        print("---------------------")


if __name__ == "__main__":
    p1 = Person("Eunice", "Female", "Food lover and currently a degree student", "public")
    p2 = Person("Josiah", "Male", "Love photography and hiking", "private")
    p3 = Person("Kay See", "Female", "A formerly known ENTP that enjoys outdoor", "public")

    # Display their profiles
    p1.display_profile()
    p2.display_profile()
    p3.display_profile()
