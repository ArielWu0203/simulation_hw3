import getopt
import sys
import numpy as np
import math
from numpy import mean

def usage():
    print(' -n # of customer \n')
    print(' -a arival rate \n')
    print(' -s service rate \n')

def exponential_rand(mean , num):
    arr = []
    
    for i in range(0,num):
        u = np.random.uniform(0,1)
        x = math.log(u)/mean*(-1)
        arr.append(x)
    
    return arr

def simulation(customer_num ,arrival_rate, service_rate):
    inter_arrival = exponential_rand(arrival_rate, customer_num)
    service_time = exponential_rand(service_rate, customer_num)
    arrive_time = [inter_arrival[0]]
    for index,value in enumerate(inter_arrival[1:]):
        arrive_time.append(arrive_time[index]+value)

    # TODO: Record Queue message in order to calculate customer waiting time
    queuing_time = []
    depart_time = []

    current_time = 0
    next_time = 0
    
    for index, value in enumerate(arrive_time):
        current_time = value
        # TODO : Server is not busy
        if current_time >= next_time :
            queuing_time.append(0)
            next_time = current_time + service_time[index]
            depart_time.append(next_time)

        # TODO : Server is busy
        else:
            queuing_time.append(next_time-current_time)
            next_time = next_time+service_time[index]
            depart_time.append(next_time)

    # TODO : calculate # of peaple in system & line
    arr_sys = [0 for n in range(int(depart_time[customer_num-1])+1) ]
    arr_line = [0 for n in range(int(depart_time[customer_num-1])+1) ]

    for index, value in enumerate(arrive_time):
        at_time = int(value)
        leave_time = int(depart_time[index])
        serve_time =  int(value+queuing_time[index])

        for t in range(at_time, leave_time):
            arr_sys[t]+=1
        for t in range(at_time, serve_time):
            arr_line[t]+=1

    print("1. Arrival rate : ",1/mean(inter_arrival))
    print("2. Service rate : ",1/mean(service_time))
    print("3. Utiliztion : ", sum(service_time)/next_time)
    print("4. Average # of customers in line : ", mean(arr_line))
    print("5. Average # of customers in system : ", mean(arr_sys))
    print("6. Average in line : ", mean(queuing_time))
    waiting_time = [depart_time[i]-arrive_time[i] for i in range(0,customer_num)]
    print("7. Average in system : ", mean(waiting_time))

if __name__ == '__main__' :
    try:
        options, args = getopt.getopt(sys.argv[1:], "hn:a:s:",[])
        arrival_rate = 0.2
        service_rate = 0.5
        customer_num = 10

        for name,value in options:
            if name in ('-h'):
                usage()
            elif name in ('-n'):
                customer_num = int(value)
            elif name in ('-a'):
                arrival_rate = float(value)
            elif name in ('-s'):
                service_rate = float(value)
        
        simulation(customer_num, arrival_rate,service_rate)
        
    
    except getopt.GetoptError:
        usage()