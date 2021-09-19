import getpass
import subprocess as sb_p
from Register_Voter import Register,showVotes

def check(id,password):
    return id == 'Admin' and password == 'admin'

def Admin_login():
    while True:
        n = int(input('''Admin Menu
1. Run Server
2. Register Voter
3. Show Votes 
4. Exit 
'''))
        if n == 1:
            sb_p.call('start python Server.py',shell=True)
            continue
        elif n == 2:
            Register()
            continue
        elif n == 3:
            showVotes()
            continue
        else: 
            break

if __name__ == "__main__":
    Admin_id = input('Admin Id: ')
    password = getpass.getpass()
    if check(Admin_id, password):
        Admin_login()
    else:
        print("Either ID or Password is Incorrect")
