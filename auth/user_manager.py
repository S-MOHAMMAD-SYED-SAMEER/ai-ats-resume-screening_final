import json


def load_users():
    with open("users.json") as f:
        return json.load(f)


def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)


def add_user(username, password, role):

    users = load_users()

    if username in users:
        return False

    users[username] = {
        "password": password,
        "role": role
    }

    save_users(users)
    return True


def change_password(username, new_password):

    users = load_users()

    if username in users:
        users[username]["password"] = new_password
        save_users(users)
        return True

    return False


def delete_user(username):

    users = load_users()

    if username == "admin":
        return False

    if username in users:
        del users[username]
        save_users(users)
        return True

    return False