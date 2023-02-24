# Створюємо порожній словник для зберігання контактів
contacts = {}

# Створюємо декоратор


def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Please enter the name and phone number separated by a space"
        except IndexError:
            return "Please enter the name of the contact"
    return wrapper


# Функція для додавання контакту
@input_error
def add_contact(data):
    name, phone = data.split(" ")
    contacts[name.lower()] = phone
    return f"{name} has been added to your contacts"

# Функція для зміни номера телефону існуючого контакту


@input_error
def change_contact(data):
    name, phone = data.split(" ")
    contacts[name.lower()] = phone
    return f"The phone number for {name} has been updated"


# Функція для виводу номера телефону за ім'ям
@input_error
def get_phone(name):

    return f"The phone number for {name} is {contacts[name.lower()]}"


# Функція для виводу всіх контактів
@input_error
def show_all():
    if len(contacts) == 0:
        return "You have no contacts"
    else:
        return "\n".join([f"{k.capitalize()}: {v}" for k, v in contacts.items()])


# Головна функція, яка взаємодіє з користувачем
def main():
    print("Hello! How can I help you?")
    while True:
        command = input(">>> ").lower()
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            data = input("Enter name and phone: ")
            print(add_contact(data))
        elif command == "change":
            data = input("Enter name and phone: ")
            print(change_contact(data))
        elif command == "phone":
            name = input("Enter name: ")
            print(get_phone(name))
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit", "."]:
            print("Good bye!")
            break
        else:
            print("Sorry, I didn't understand the command. Please try again.")


# Запускаємо головну функцію
if __name__ == '__main__':
    main()
