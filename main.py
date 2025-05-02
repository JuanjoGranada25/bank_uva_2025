def add_user(users):
    name = input("Complete name: ")
    email = input("Email: ")
    born_day = input("Born Day (DD/MM/AAAA): ")
    gender = input("Gender: ")
    password = input("Password: ")

    new_user = (name, email, born_day, gender, password)
    users.append(new_user)
    return users



def main():
    users = []
    users = add_user(users)
    print(users)

main()