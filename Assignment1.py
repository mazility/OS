def main():
    print('\n\nPlease select the number of CPU scheduling options below\n1: FCFS\n2: Preemptive SJF\n3: Priority\n4: Round Robin')
    selection = 0
    while not selection:
        try:
            selection = int(input('\nPlease select the options and enter the number of it: \n'))
            if selection not in (1, 2, 3, 4):
                raise ValueError
        except ValueError:
            selection = 0
            print("That's not an option!")

    if selection == 1:
        FCFS()
    elif selection == 2:
        SRTF()
    elif selection == 3:
        Priority()
    else:
        RoundR()


def FCFS():
    inp = int(input('Enter the numbers of process: '))

    proc = []
    for i in range(0, inp):
        proc.insert(i, i + 1)

    print("Enter the burst time of the process with spaces: \n")
    bt = list(map(int, input().split()))
    wt = list()
    wt.append(0)
    avgwt = 0
    temp = 0

    for i in range(0, len(bt)):
        if i > 0:
            temp += bt[i-1]
            wt.append(bt[i] + temp)
        wt.append(bt[i] + temp)
        avgwt += wt[i]
    avgwt = float(avgwt)/inp
    print("\n")
    print("Process\t  Burst Time\t  Waiting Time")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t\t" + str(wt[i]))
    print("Average Waiting time is: " + str(avgwt))


def SRTF():
    inp = int(input('Enter number of processes: '))
    wt = list()
    print('Enter the burst time of process with spaces: \n')
    bt = list(map(int, input().split()))
    res_bt = list()
    proc = []
    premp = []
    for i in range(0, inp):
        if i == 0:
            if bt[0] > bt[1]:
                wt.insert(0, 1)
        wt.append(0)
        res_bt.append(bt[i])
        proc.insert(i, i + 1)
        premp.insert(i, i)
    for i in range(0, len(bt) - 1):
        if bt[0] > bt[1]:
            bt[i] -= 1
        for j in range(0, len(bt) - i - 1):
            if bt[j] > bt[j+1]:
                temp = bt[j]
                bt[j] = bt[j+1]
                bt[j+1] = temp
                temp2 = premp[j]
                premp[j] = premp[j+1]
                premp[j+1] = temp2

    for i in range(0, inp):
        if i == 0:
            if bt[0] > bt[1]:
                wt.pop(i + 1)
        wt.insert(i + 1, bt[i])
        temp = wt[i+1]
        wt.pop(i + 1)
        wt.insert(i + 1, wt[i] + temp)

    rev_wt, rev_premp = list(), list()
    for i in range(0, len(bt)):
        rev_wt.append(wt[i])
        rev_premp.append(premp[i])
    print(rev_premp,rev_wt)

    for i in range(0, len(bt) - 1):
        for j in range(0, len(bt) - i - 1):
            if rev_premp[j] > rev_premp[j+1]:
                temp = rev_premp[j]
                rev_premp[j] = rev_premp[j+1]
                rev_premp[j+1] = temp
                temp = rev_wt[j]
                rev_wt[j] = rev_wt[j + 1]
                rev_wt[j + 1] = temp
    print(rev_premp, rev_wt)

    for i in range(0, 1):
        if rev_wt[i] > rev_wt[i+1]:
            rev_wt[i] -= 1
    print(rev_premp, rev_wt)

    avgwt = 0
    for i in range(0, inp):
        avgwt += rev_wt[i] - rev_premp[i]

    avgwt = float(avgwt)/inp
    print("\n")
    print("Process\t  Burst Time\t  Waiting Time")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(res_bt[i]) + "\t\t\t\t" + str(rev_wt[i]))
    print("Average Waiting time is: " + str(avgwt))


def Priority():
    print("Enter the numbers of process: ")
    inp = int(input())
    proc = []
    for i in range(0, inp):
        proc.insert(i, i + 1)

    print("\nEnter the burst time of the process with spaces: \n")
    bt = list(map(int, input().split()))

    print("\nEnter the priority of the process with spaces: \n")
    prio = list(map(int, input().split()))

    wt = []

    for i in range(0, len(prio) - 1):
        for j in range(0, len(prio) - i - 1):
            if (prio[j] > prio[j + 1]):
                temp = prio[j]
                prio[j] = prio[j + 1]
                prio[j + 1] = temp

                temp = bt[j]
                bt[j] = bt[j + 1]
                bt[j + 1] = temp

                temp = proc[j]
                proc[j] = proc[j + 1]
                proc[j + 1] = temp
    wt.insert(0, 0)

    for i in range(1, len(proc)):
        wt.insert(i, wt[i - 1] + bt[i - 1])
        print(wt[i - 1], "\t ", bt[i-1])

    avgwt = 0
    for i in range(0, len(proc)):
        avgwt = avgwt + wt[i]

    avgwt = float(avgwt) / inp

    print("\n")
    print("Process\t  Burst Time\t  Waiting Time\t Priority")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t\t" + str(wt[i]) + "\t\t\t\t" + str(prio[i]))
    print("Average Waiting time is: " + str(avgwt))


def RoundR():
    print("Enter the numbers of process: ")
    inp = int(input())
    proc = list()
    for i in range(0, inp):
        proc.insert(i, i + 1)
    print("\nEnter the burst time of the process with spaces: \n")
    bt = list(map(int, input().split()))
    print("\nEnter the time quantum value: ")
    tq = int(input())
    stopper, counter = 0, 0
    res_arr, res_temp, res_bt = list(), list(), list()
    res_c = list()
    res_temp.append(0)
    for i in range(0, len(bt)):
        res_bt.append(bt[i])
        res_c.append(0)
        res_arr.append(bt[i])
        stopper += bt[i]

    temp_proc1 = list()
    temp_proc1.append(0)
    i = 0
    while i <= len(bt):
        for j in range(0, len(bt)):
            if bt[j] > tq:
                if j == 0:
                    temp = temp_proc1[j]
                    temp_proc1.pop(j)
                    temp_proc1.insert(j, temp + tq)
                res_c.pop(j)
                res_c.insert(j, counter)
                res_arr.pop(j)
                res_arr.insert(j, counter)
                bt[j] -= tq
                counter += tq
            elif bt[j] <= tq and bt[j] != 0:
                temp = bt[j]
                res_c.pop(j)
                res_c.insert(j, counter)
                res_arr.pop(j)
                res_arr.insert(j, counter)
                bt[j] -= bt[j]
                counter += int(temp)
        if stopper == counter:
            i += len(bt) + 1
    avgwt = 0
    t = 0
    for i in range(0, len(bt)):
        if i == 0:
            t += res_arr[i]
            res_arr.pop(i)
            res_arr.insert(i, t - temp_proc1[i])
        avgwt += res_arr[i]

    avgwt = float(avgwt) / inp
    print("Process\t  Burst Time\t  Waiting Time")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(res_bt[i]) + "\t\t\t\t" + str(res_arr[i]))
    print("Average Waiting time is: " + str(avgwt))



if __name__ == '__main__':
    main()
