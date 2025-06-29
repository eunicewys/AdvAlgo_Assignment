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
        self.users = []

    def add_user(self, person):
        if person.get_name() not in self.graph:
            self.graph[person.get_name()] = []
            self.users.append(person)

    def add_follow(self, follower_name, following_name):
        if follower_name not in self.graph or following_name not in self.graph:
            print("One or both users do not exist.")
            return
        if following_name not in self.graph[follower_name]:
            self.graph[follower_name].append(following_name)
            print(f"{follower_name} is now following {following_name}.")
        else:
            print(f"{follower_name} already follows {following_name}.")

    def remove_follow(self, follower_name, following_name):
        if follower_name in self.graph and following_name in self.graph[follower_name]:
            self.graph[follower_name].remove(following_name)
            print(f"{follower_name} has unfollowed {following_name}.")
        else:
            print("The follow relationship does not exist.")

    def view_all_users(self):
        print("\n--- List of All Users ---")
        for user in self.users:
            print(f"- {user.get_name()}")

    def view_profile_ignore_privacy(self, name):
        for user in self.users:
            if user.get_name() == name:
                print("\n--- Profile (Privacy Ignored) ---")
                print(f"Name    : {user.get_name()}")
                print(f"Gender  : {user.get_gender()}")
                print(f"Bio     : {user.get_bio()}")
                print(f"Privacy : {user.get_privacy().capitalize()}")
                return
        print("User not found.")

    def view_profile_with_privacy(self, name):
        for user in self.users:
            if user.get_name() == name:
                print("\n--- Profile View ---")
                print(f"Name    : {user.get_name()}")
                if user.get_privacy() == "private":
                    print("Gender  : [Private]")
                    print("Bio     : [This profile is private]")
                else:
                    print(f"Gender  : {user.get_gender()}")
                    print(f"Bio     : {user.get_bio()}")
                return
        print("User not found.")

    def view_followers(self, name):
        followers = [user for user, followings in self.graph.items() if name in followings]
        print(f"\n--- Followers of {name} ---")
        if followers:
            for f in followers:
                print(f"- {f}")
        else:
            print("- No followers")

    def view_following(self, name):
        print(f"\n--- {name} is following ---")
        following = self.graph.get(name, [])
        if following:
            for f in following:
                print(f"- {f}")
        else:
            print("- Not following anyone")

    def user_exists(self, name):
        return name in self.graph

    def get_all_usernames(self):
        return [u.get_name() for u in self.users]



def main():
    smg = SocialMediaGraph()

    preload = [
        Person("Rachel", "Female", "*****", "private"),
        Person("Cara", "Female", "Just a normal person", "public"),
        Person("Jaeson", "Male", "Loves coding", "public"),
        Person("Kelvan", "Male", "Gym rat & gamer", "public"),
        Person("Elon", "Male", "Futurist", "public"),
    ]
    for p in preload:
        smg.add_user(p)


    smg.add_follow("Rachel", "Cara")
    smg.add_follow("Rachel", "Jaeson")
    smg.add_follow("Rachel", "Elon")
    smg.add_follow("Elon", "Rachel")
    smg.add_follow("Elon", "Calvin")
    smg.add_follow("Jaeson", "Rachel")
    smg.add_follow("Jaeson", "Cara")


    while True:
        print("\n" + "=" * 50)
        print("Instaframe - Socialing System")
        print("=" * 50)
        print("1. View All Users")
        print("2. View Profile (Ignore Privacy)")
        print("3. View Profile (Respect Privacy)")
        print("4. View Someone's Followers")
        print("5. View Who Someone is Following")
        print("6. Add New User")
        print("7. Follow Someone")
        print("8. Unfollow Someone")
        print("9. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            smg.view_all_users()

        elif choice == "2":
            name = input("Enter the name of the user to view (ignore privacy): ").strip()
            smg.view_profile_ignore_privacy(name)

        elif choice == "3":
            name = input("Enter the name of the user to view: ").strip()
            smg.view_profile_with_privacy(name)

        elif choice == "4":
            name = input("Enter the name of the user to check followers: ").strip()
            if smg.user_exists(name):
                smg.view_followers(name)
            else:
                print("User not found.")

        elif choice == "5":
            name = input("Enter the name of the user to check following list: ").strip()
            if smg.user_exists(name):
                smg.view_following(name)
            else:
                print("User not found.")

        elif choice == "6":
            name = input("Enter new user's name: ").strip()
            if smg.user_exists(name):
                print("User already exists.")
                continue
            gender = input("Enter gender: ").strip()
            bio = input("Enter biography: ").strip()
            privacy = input("Privacy (public/private): ").strip().lower()
            if privacy not in ["public", "private"]:
                print("Invalid privacy setting. Defaulting to public.")
                privacy = "public"
            new_user = Person(name, gender, bio, privacy)
            smg.add_user(new_user)
            print(f"User '{name}' added successfully!")

        elif choice == "7":
            u1 = input("Enter follower's name: ").strip()
            u2 = input("Enter person to follow: ").strip()
            smg.add_follow(u1, u2)

        elif choice == "8":
            u1 = input("Enter unfollower's name: ").strip()
            u2 = input("Enter person to unfollow: ").strip()
            smg.remove_follow(u1, u2)

        elif choice == "9":
            print("Thanks for using Instaframe!")
            break

        else:
            print("Invalid choice. Please enter 1–9.")


if __name__ == "__main__":
    main()
