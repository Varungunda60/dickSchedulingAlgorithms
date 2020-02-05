import socket
import Add
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1424))
while True:
    choice=input("You can select following\n 1.FCFS\n2.SSTF\n3.SCAN\n4.CSCAN\n5.LOOK\n6.CLOOK\n7.EXIT")
    s.send(bytes(choice,"UTF-8"))
    if choice == '7':
        break
    i=input('do you want to continue[y/n]')
    if i!='y' or i!='Y':
        exit()



