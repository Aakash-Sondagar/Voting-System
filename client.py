import getpass
import socket

def voteCast(vote,client_socket):
    client_socket.send(vote.encode()) 

    message = client_socket.recv(1024) 
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        print("Vote Casted Successfully")
    else:
        print("Vote Cast Failed... \nTry again")
    client_socket.close()

list = {
    1:'bjp', 2:'cong', 3:'aap', 4:'ss', 5:'nota'
}

def votingPg(client_socket):
    n = int(input('''
List
1. BJP
2. Congress
3. AAP
4. Shiv Seva
5. Nota
'''))
    if n < 1 or n > 5:
        print('Invalid Vote')
    else:
         voteCast(list[n],client_socket)

def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'

def failed_return(client_socket,message):
    message = message + "... \nTry again..."
    print(message)
    client_socket.close()

def log_server(client_socket,voter_ID,password):
    message = voter_ID + " " + password
    client_socket.send(message.encode()) #2

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        votingPg(client_socket)

    elif(message=="VoteCasted"):
        message = "Vote has Already been Cast"
        failed_return(client_socket,message)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter"
        failed_return(client_socket,message)

    else:
        message = "Server Error"
        failed_return(client_socket,message)


def voterLogin():
    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(client_socket,message)

    voter_id = input("Voter ID: ")
    password = getpass.getpass()
    log_server(client_socket,voter_id,password) 



if __name__ == "__main__":
    voterLogin()