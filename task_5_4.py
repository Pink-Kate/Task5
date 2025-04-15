def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "Enter the argument for the command"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return f"{name}:{contacts[name]}"

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}:{phone}\n"
    return result.split()    

@input_error
def parse_command(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    contacts = {}

    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": lambda args, contacts: show_all(contacts),
        "exit": None,
        "close": None,
        "good bye": None
    }  

    print('Hello')
    while True:
        user_input = input("enter a command:").strip()

        if user_input.lower() in ("exit", "close", "good bye"):
            print("BB")
            break

        parts = user_input.split()
        command = parts[0].lower()
        args = parts[1:]

        handler = commands.get(command)

        if handler:
            print(handler(args, contacts))
        else:
            print("Unknow command")

if __name__ == "__main__":
    main()            
