import socket
from threading import Thread
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port = 5000
server.bind((ip_address,port))
server.listen()
listOfClients = []
nicknames = []
print("SERVER HAS STARTED")

def ct(con,nickname):
    con.send("Welcome to the Chat !!!".encode("utf-8"))
    while True:
        try:
            message = con.recv(2048).decode("urf-8")
            if(message):
                print(message)
                broadcast(message,con)
            else:
                remove(con)
                remove_nickname(nickname)
        except:
            continue            
def broadcast(message,connection):
    for clients in listOfClients:
        if clients!=connection:
            try:
                clients.send(message.encode("utf-8"))
            except:
                remove(clients)    
def remove(connection):
    if connection in listOfClients:
        listOfClients.remove(connection)
def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)
while True:
    con,addr = server.accept()
    con.send("Nickname".encode("utf-8"))
    nickname = con.recv(2048).decode("utf-8")
    listOfClients.append(con)
    nicknames.append(nickname)
    message = "{} Joined !! ".format(nickname)
    print(message)
    broadcast(message,con)
    newThread = Thread(target = ct,args=(con,nickname))  
    newThread.start()    


