def parse_input(user_input):
    # Розбираємо ввід на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command format. Use 'add [name] [phone]'."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command format. Use 'change [name] [new phone]'."
    name, new_phone = args
    if name not in contacts:
        return f"Contact with name '{name}' not found."
    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) < 1:
        return "Invalid command format. Use 'phone [name]'."
    name = args[0]
    if name not in contacts:
        return f"Contact with name '{name}' not found."
    return f"{name}'s phone: {contacts[name]}"

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return result

def main():
    contacts = {}  # Словник для зберігання контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
