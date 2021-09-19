import socket
import threading
from threading import Thread
from function import *

lock = threading.Lock()

def client_thread(connection):
    data = connection.recv(1024) 
    log = (data.decode()).split(' ')
    log[0] = int(log[0])
    if(verify(log[0],log[1])): 
        if(isEligible(log[0])):
            print('Voter Logged in... ID:'+str(log[0]))
            connection.send("Authenticate".encode())
        else:
            print('Vote Already Cast by ID:'+str(log[0]))
            connection.send("VoteCasted".encode())
    else:
        print('Invalid Voter')
        connection.send("InvalidVoter".encode())

    data = connection.recv(1024)                                    
    print("Vote Received from ID: "+str(log[0])+"  Processing...")
    lock.acquire()

    if(vote_update(data.decode(),log[0])):
        print("Vote Casted Sucessfully by voter ID = "+str(log[0]))
        connection.send("Successful".encode())
    else:
        print("Vote Update Failed by voter ID = "+str(log[0]))
        connection.send("Vote Update Failed".encode())

    lock.release()
    connection.close()

def Server():
    server_socket = socket.socket()
    host = socket.gethostname()
    port = 4001

    ThreadCount = 0

    try:
        server_socket.bind((host,port))
    except socket.error as e:
        print(str(e))

    print("Waiting for the connection")
    server_socket.listen(10)
    print( "Listening on " + str(host) + ":" + str(port))

    while True:
        client,address = server_socket.accept()
        print('Connected to :', address)
        client.send("Connection Established".encode())

        t = Thread(target = client_thread,args = (client,))
        t.start()
        ThreadCount+=1

    server_socket.close()

if __name__ == "__main__":
    Server()