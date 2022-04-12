from cryptography.fernet import Fernet
 # module that will allow you to encrypt text


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def view():
    with open('passwords.txt', 'r') as f:    #using with here allows us to not use file.open and then having to close it with file.close, with automatically does it.
        # 'r' mode allows us to read the file
         for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:    #using with here allows us to not use file.open and then having to close it with file.close, with automatically does it.
        # 'a' mode allows us to append the file
          f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue




while True:
    mode = input("Would you like to add a new password or view existing ones (view/add/) or enter Q to quit : ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Enter a valid option.")
        continue 
    
