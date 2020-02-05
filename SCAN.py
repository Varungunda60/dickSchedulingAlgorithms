import matplotlib.pyplot as plt
def SCAN(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	y=[]
	lists=[]
	val=0
	y.append(time)
	lists.append(hp)
	end=200
	start=0
	#seek from curr_pos to end which is 200
	for i in range(pos,end+1):
		if i in requests:
			val=val+2
			y.append(val)
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			lists.append(i)
			requests.remove(i)

	time+=abs(pos-end)
	pos=end
	#seek back to start
	for i in range(end,start-1,-1):
		if i in requests:
			val=val+2
			y.append(val)
			time+=abs(pos-i)
			# print(time)
			pos=i
			print("        ",i,"  seeked")
			lists.append(i)
			requests.remove(i)
	print(time)
	plt.plot(lists,y)
	plt.show()
	# calculate average seek time
	avg_seek_time = time/n
	return avg_seek_time


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

    #print(" Fcfs")
    print("Avg seek time for SCAN was ",SCAN(hp, requests))
