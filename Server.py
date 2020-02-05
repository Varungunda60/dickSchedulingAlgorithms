#server
import socket
from disk1 import *
from SCAN import *
from C_SCAN import *
from LOOK import *
from C_LOOK import *
from SSTF import *
import matplotlib.pyplot as plt

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1424))
s.listen(5)
while True:
    clt,addr=s.accept()
    print(f"connectionn  to {addr} established")
    while True:
        algo=clt.recv(1024).decode("utf-8")
        print(type(algo))
        print("Provide number of I/O requests")

        n = int(input())
        print("Provide initial position of disc arm (total cylinders=200)")
        hp = int(input())
        while hp > 200:
            print("INVALID !!! try again")
            hp = int(input())
        print("Provide positions to visit : max is 200")
        requests = []
        for i in range(n):
            req = int(input())
            requests.append(req)

        print(requests)
        if algo=='1':
            #print("i am here")
            print("Average seek time for FCFS is ",FCFS(hp,requests))
        elif algo=='2':
            print("Average seek time for SSTF is ",SSTF(hp,requests))
        elif algo=='3':
            #SCAN(hp,requests)
            print("Average seek time for SCAN is ",SCAN(hp,requests))
        elif algo=='4':
            #C_SCAN(hp,requests)
            print("Average seek time for C_SCAN is  ",C_SCAN(hp,requests))
        elif algo=='5':
            #LOOK(hp,requests)
            print("Average seek time for LOOK is  ",LOOK(hp,requests))
        elif algo=='6':
            #C_LOOK(hp,requests)
            print("Average seek time for C_LOOK is ",C_LOOK(hp,requests))
        else:
            break

        s1=input("do you wnat to continue(y/n)")
        if (s1=='n')or(s1=='N'):
            exit()

s.close()
exit()
