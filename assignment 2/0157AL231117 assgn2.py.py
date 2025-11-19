'''

NAME- LAKSHYA MANSHARAMANI 
ENROLLEMENT NO.- 0157AL231117
BATCH- CSE AIML (5TH SEM)
(TNP-(MTF)) - 10:30 A.M.


'''

logged_user = ''
logged = False
users={}
def register():
    global users
    username=input("Enter your username: ")
    if username in users:
        print("this username already exists")
        return
    password= input("enter a strong password ")
    users[username] = password
    print(f"your username is {username}")




def login():
    global logged,logged_user,users
    if logged==True:
        print ("you are already logged in")
        return
    username=input('enter your username: ')
    password=input("enter your password: ")
    if users.get(username)==password:
        logged=True
        logged_user=username
        print("sucessfully logined")
    else:
        print ("invalid password")


def show_profile():
    global logged,logged_user
    if logged==True:
        print(f"hi welcome back{logged_user}")
    else:
        print("you are not logined yet")
        login()


def update_profile():
    global users,logged,logged_user
    if logged==True:
        new_password=input("enter the new password: ")
        users[logged_user]=new_password
        print("Password updated successfully.")
    else:
        print("you are not loginned yet")
        login()

def logout():
    global users, logged, logged_user
    if logged==True:
        logged=False
        logged_user=''
        print("you are officially logged out")
    else:
        print("Already logged out ")


def terminate():
    print("Exiting program. Goodbye!")
    exit()

def main():
    while True:
        print("\n Welcome in LNCT ")
        response = input('''\n
                Choose option:
                1. Registration
                2. Login
                3. Profile
                4. Update profile
                5. Logout
                6. Main Menu (Reload)
                7. Exit

                Select option (1/2/3/4/5/6/7):   ''')

        if response == '1':
            register()
        elif response == '2':
            login()
        elif response == '3':
            show_profile()
        elif response == '4':
            update_profile()
        elif response == '5':
            logout()
        elif response == '6':
            continue  # just reloads main menu
        elif response == '7':
            terminate()
        else:
            print("Invalid choice! Please try again.")

main()
