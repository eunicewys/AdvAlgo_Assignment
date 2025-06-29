class Person:
    def __init__(self, name, gender, bio, privacy="public"):
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy.lower()

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_bio(self):
        return self.bio

    def get_privacy(self):
        return self.privacy


class SocialMediaGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, person):
        if person.get_name() not in self.graph:
            self.graph[person.get_name()] = []

    def add_follow(self, follower, following):
        follower_name = follower.get_name()
        following_name = following.get_name()

        if follower_name not in self.graph:
            self.add_user(follower)
        if following_name not in self.graph:
            self.add_user(following)

        if following_name not in self.graph[follower_name]:
            self.graph[follower_name].append(following_name)

    def display_profile(self, people, index):
        if index < 0 or index >= len(people):
            print("Invalid selection.")
            return

        person = people[index]
        print("\n" + "=" * 40)
        print("         Profile Details")
        print("=" * 40)
        print(f"Name     : {person.get_name()}")
        if person.get_privacy() == "private":
            print("Biography: [This profile is private]")
        else:
            print(f"Biography: {person.get_bio()}")
        print("=" * 40)

    def view_followers(self, username):
        followers = []
        for user, following_list in self.graph.items():
            if username in following_list:
                followers.append(user)
        return followers

    def view_following(self, username):
        return self.graph.get(username, [])



if __name__ == "__main__":
    people = []

    people.append(Person("Rachel", "Female", "*****", "private"))
    people.append(Person("Cara", "Female", "Just a normal person", "public"))
    people.append(Person("Jaeson", "Male", "Loves coding", "public"))
    people.append(Person("Kelvan", "Male", "Gym rat & gamer", "public"))
    people.append(Person("Ahmad", "Male", "Futurist", "public"))

    gram = SocialMediaGraph()
    for person in people:
        gram.add_user(person)

    gram.add_follow(people[0], people[1])  # Rachel ➝ Cara
    gram.add_follow(people[0], people[2])  # Rachel ➝ Jaeson
    gram.add_follow(people[0], people[4])  # Rachel ➝ Ahmad
    gram.add_follow(people[4], people[0])  # Ahmad ➝ Rachel
    gram.add_follow(people[4], people[3])  # Ahmad ➝ Kelvan
    gram.add_follow(people[2], people[0])  # Jaeson ➝ Rachel
    gram.add_follow(people[2], people[1])  # Jaeson ➝ Cara


    while True:
        print("\n" + "*" * 50)
        print("Welcome to Instaframe - Social Graph Explorer")
        print("*" * 50)
        print("Select an option:")
        print("1. View Profile Details")
        print("2. View Followers of a Person")
        print("3. View Following List of a Person")
        print("4. Exit")
        print("*" * 50)

        choice = input("Enter your choice (1-4): ")

        if choice == "4":
            print("\nThank you for using InstaLite!")
            break

        print("\nAvailable Profiles:")
        for i, person in enumerate(people, 1):
            print(f"{i}. {person.get_name()}")

        try:
            index = int(input("Select a profile (1-5): ")) - 1
            if index < 0 or index >= len(people):
                print("Invalid selection. Try again.")
                continue

            selected = people[index]
            username = selected.get_name()

            if choice == "1":
                gram.display_profile(people, index)

            elif choice == "2":
                print("\n" + "=" * 40)
                print(f"Followers of {username}:")
                followers = gram.view_followers(username)
                if followers:
                    for f in followers:
                        print(f"- {f}")
                else:
                    print("- No followers yet.")
                print("=" * 40)

            elif choice == "3":
                print("\n" + "=" * 40)
                print(f"{username} is following:")
                following = gram.view_following(username)
                if following:
                    for f in following:
                        print(f"- {f}")
                else:
                    print("- Not following anyone.")
                print("=" * 40)

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")
