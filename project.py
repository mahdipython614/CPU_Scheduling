import os
from round_robin_update import RoundRobin
from fcfs_update import FcFs
import string
import re

file = input('enter a name file:\n')
Algorithm = eval(input('Select the option:\n1.FCFS\n2.round robin\n'))

#for Queue data in fcfs
def order(dataproces):
    Queue = 0
    Queuedata=dataproces.copy()
    dataproces=[]
    while sorted(dataproces) != sorted(Queuedata):
        for proces in range(int(len(Queuedata)/4)):
            if int(Queuedata[(4*proces)+2])==Queue:
                dataproces.extend(Queuedata[proces*4:(proces+1)*4])

        Queue += 1
    return dataproces

def printData_fcfs():
    print("Processes   Burst Time   Arrival Time   Waiting",
          "Time   Turn-Around Time   Completion Time \n")
    total_wt = 0
    total_tat = 0
    id = [dataproces[(k * 4) + 1] for k in range(int(len(dataproces) / 4))]
    name = [dataproces[k * 4] for k in range(int(len(dataproces) / 4))]
    processes = [i + ' - ' + j for i, j in zip(*[id, name])]
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        print(" ", processes[i], "\t\t\t", bt[i], "\t\t\t", at[i],
              "\t\t\t", wt[i], "\t\t\t ", tat[i], "\t\t\t ", compl_time)

    print("Average waiting time = %.5f " % (total_wt / n))
    print("\nAverage turn around time = ", total_tat / n)


def write_fcfs():
    if 'output_fcfs.txt' in os.listdir(os.getcwd()):
        mode = 'a'
    else:
        mode = 'w'
    with open('output_fcfs.txt', mode) as fcfsfile:
        fcfsfile.write("\nProcesses   Burst Time   Arrival Time   Waiting Time   Turn-Around Time   Completion Time \n")
        total_wt = 0
        total_tat = 0
        id = [dataproces[(k * 4) + 1] for k in range(int(len(dataproces) / 4))]
        name = [dataproces[k * 4] for k in range(int(len(dataproces) / 4))]
        processes = [i + ' - ' + j for i, j in zip(*[id, name])]
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            compl_time = tat[i] + at[i]
            fcfsfile.write(" " + processes[i] + '	' + str(bt[i]) + '		' + str(at[i]) + '		' + str(
                wt[i]) + '		' + str(tat[i]) + '		' + str(compl_time) + '\n')

        fcfsfile.write("\nAverage waiting time = %.5f " % (total_wt / n))
        fcfsfile.write("\nAverage turn around time = " + str(total_tat / n))


def printData_rr():
    print('slice_time:' + str(slice_time))
    print(
        "Process_ID  Arrival_Time  Completed  Original_Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time")
    for i in range(len(process_data)):
        for j in range(len(process_data[i])):
            if j!=2:
                print(process_data[i][j], end="\t\t\t\t")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')

    print(f'Average Waiting Time: {average_waiting_time}')

    #print(f'Sequence of Processes: {executed_process}')


def write_rr():
    if 'output_rr.txt' in os.listdir(os.getcwd()):
        mode = 'a'
    else:
        mode = 'w'
    with open('output_rr.txt', mode) as output_file:
        output_file.write('slice_time:' + str(slice_time) + '\n')
        output_file.write(
            "Process_ID  Arrival_Time   Completed  Original_Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time\n")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                if j != 2:
                    output_file.write(str(process_data[i][j]) + '		')
            output_file.write('\n')

        output_file.write(f'Average Turnaround Time: {average_turnaround_time}\n')

        output_file.write(f'Average Waiting Time: {average_waiting_time}\n')

        output_file.write(f'Sequence of Processes: {executed_process}\n')
        output_file.close()


def listData(dataproces):
    for info in range(int(len(dataproces) / 4)):
        one_pro = dataproces[:4]
        data.append(one_pro)
        dataproces = dataproces[4:]


def new_file(dataproces):
    new_file = input('enter a name file:\n')
    with open(new_file, 'r') as nf:
        new_data = re.sub('[' + string.punctuation + ']', ' ', nf.read()).split()
    if Algorithm == 2:
        listData(new_data)
    if Algorithm == 1:
        dataproces.extend(new_data)
        return order(dataproces)


def input_fcfc():
    id = [dataproces[(k * 4) + 1] for k in range(int(len(dataproces) / 4))]
    name = [dataproces[k * 4] for k in range(int(len(dataproces) / 4))]
    processes = [i + ' - ' + j for i, j in zip(*[id, name])]
    n = int(len(dataproces) / 4)
    burst_time = [int(dataproces[(4 * k) + 3]) for k in range(int(len(dataproces) / 4))]
    arrival_time = [int(dataproces[(4 * k) + 2]) for k in range(int(len(dataproces) / 4))]
    return processes, n, burst_time, arrival_time


with open(file, 'r') as f:
    dataproces = re.sub('[' + string.punctuation + ']', ' ', f.read()).split()
if Algorithm == 1:
    fcfs = FcFs()
    dataproces=order(dataproces)
    processes, n, burst_time, arrival_time = input_fcfc()
    try:
        wt, tat, at, bt = fcfs.findavgTime(processes, n, burst_time,
                                           arrival_time)
    except KeyboardInterrupt:
        dataproces=new_file(dataproces)
        processes, n, burst_time, arrival_time = input_fcfc()
        wt, tat, at, bt = fcfs.findavgTime(processes, n, burst_time,
                                           arrival_time)

    printData_fcfs()
    write_fcfs()


elif Algorithm == 2:
    rr = RoundRobin()
    data = []
    listData(dataproces)
    for slice_time in [1, 5, 8]:
        try:
            rr.processData(data, slice_time)
        except KeyboardInterrupt:
            new_file(dataproces)
            rr.processData(data, slice_time)
        process_data, average_turnaround_time, average_waiting_time, executed_process = rr.getData()
        process_data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        printData_rr()
        write_rr()
