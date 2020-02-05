from heapq import *
import matplotlib.pyplot as plt


def FCFS(hp, requests):
    time = 0
    lists = []
    lists.append(hp)
    y = []
    y.append(0)
    n = len(requests)
    pos = hp
    val=2
    for request in requests:
        time += abs(request - pos)
        pos = request
        lists.append(pos)
        print("        ", pos, "  seeked")
        val = val+2
        y.append(val)
    print(lists,y)
    plt.plot(lists, y)
    plt.show()
    return time/n

if __name__ == '__main__':
    print("DISK SCHEDULING:")
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

    print(" Fcfs")
    print("Avg seek time for  fcfs was ",FCFS(hp, requests))