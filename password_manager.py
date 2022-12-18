from cryptography.fernet import Fernet
# pass statement is used as a placeholder for future code
# rstrip strips off the carriage return from the line
# split the string "ad|cd|ef" = ["ad", "cd", "ef"]
# assign the first element in the list to user and the next to passw
# def to define a function
# if we open a file we should close it 'with' automatically closes the file
# open a file in a-append w-write(override), r-read
# once we call the function write_key() we are gonna comment it with ''' for multiline
# what encode() does is takes the string and convert into bytes
# byte string is represented as b'hello', byte rep of hello
# we have decode() to decode to the regular string

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)  # initialize the module


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view,add)?, press q to quit ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
