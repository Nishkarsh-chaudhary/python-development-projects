from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_files:
        # key_files.write(key)'''
        
        
def load_key():
    
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


Master_pwd = input("what is the master password? ")
key = load_key() + Master_pwd.encode()
fer = Fernet(key)

def view():
      with open('password.txt', 'r') as f:
       for line in f.readlines():
           data = line.rstrip()
           user , passw = data.split("|")
           print("user:",user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input("would you like to add the new password or view existing one ? or press q to quite (view/add/q)").lower()

    if mode == "q":
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("invalid choice ")
        continue