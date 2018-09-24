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
    inp = int(input('Enter the number of process: \n'))

    proc, premp,r_bt1, r_bt2, r_bt3, proc_bt, res_bt, wt = [], [], [], [], [], [], [], []
    for i in range(0, inp):
        proc.append(i + 1)
        premp.append(i)
        r_bt1.append(0)
        r_bt2.append(0)

    print('Enter the burst time of the process with spaces: \n')
    bt = list(map(int, input().split()))

    bt_sort1, bt_sort2, bt_sort3 = [], [], []
    for i in range(0, len(bt)):
        bt_sort1.append(bt[i])
        bt_sort2.append(bt[i])
        bt_sort3.append(bt[i])

    for i in range(0, len(bt)-1):
        for j in range(0, len(bt) - i - 1):
            if bt_sort1[j] > bt_sort1[j+1]:
                temp = bt_sort1[j]
                bt_sort1[j] = bt_sort1[j+1]
                bt_sort1[j+1] = temp
    smallest_bt = bt_sort1[0]
    smallest_marker = 0

    for i in range(0, len(bt_sort1)):
        smallest_marker = bt_sort2.index(smallest_bt)

    for i in range(0, len(bt)-1):
        for j in range(0, len(bt) - i - 1):
            if bt_sort2[j] > bt_sort2[j+1]:
                temp = bt_sort2[j]
                bt_sort2[j] = bt_sort2[j+1]
                bt_sort2[j+1] = temp
                if i < smallest_marker and j+1 == smallest_marker:
                    temp = r_bt1[i]
                    r_bt1.pop(i)
                    r_bt1.insert(i, temp + 1)
                    wt.insert(i, 1)

    for i in range(0, len(bt)):
        res_bt.append(bt_sort3[i] - r_bt1[i])

    for i in range(0, len(bt)-1):
        for j in range(0, len(bt) - i - 1):
            if res_bt[j] == res_bt[j+1]:
                if res_bt[i] == res_bt[smallest_marker] and res_bt[j+1] == res_bt[smallest_marker]:
                    temp = r_bt2[i]
                    r_bt2.pop(i)
                    r_bt2.insert(i, temp + 1)

    for i in range(0, len(bt)):
        r_bt3.append(r_bt1[i] - r_bt2[i])

    for i in range(0, len(bt)-1):
        for j in range(0, len(bt) - i - 1):
            if res_bt[j] > res_bt[j+1]:
                temp = res_bt[j]
                res_bt[j] = res_bt[j+1]
                res_bt[j+1] = temp
                temp = premp[j]
                premp[j] = premp[j+1]
                premp[j+1] = temp

    lenr_bt3 = 0
    for i in range(0, len(bt)):
        lenr_bt3 += r_bt3[i]

    for i in range(0, len(bt)):
        wt.append(res_bt[i])

    f_wt = []
    if len(bt)+lenr_bt3 < len(wt):
        for i in range(0, len(bt) - 1 + lenr_bt3):
            temp = wt[i]
            if i == 0:
                f_wt.append(temp)
            f_wt.append(f_wt[i] + wt[i + 1])
    else:
        for i in range(0, len(bt) - 1):
            temp = wt[i]
            if i == 0:
                f_wt.append(temp)
            f_wt.append(f_wt[i] + wt[i + 1])

    for i in range(0, lenr_bt3):
        if len(bt) < len(f_wt):
            f_wt.pop(0)

    for i in range(0, len(bt)-1):
        for j in range(0, len(bt) - i - 1):
            if premp[j] > premp[j+1]:
                temp = f_wt[j]
                f_wt[j] = f_wt[j+1]
                f_wt[j+1] = temp
                temp = premp[j]
                premp[j] = premp[j+1]
                premp[j+1] = temp

    final_wt = []
    for i in range(0, len(bt)):
        final_wt.append(f_wt[i] - r_bt2[i] - r_bt3[i] - premp[i])
    print(final_wt)

    avgwt = 0
    for i in range(0, len(bt)):
        avgwt += final_wt[i]
    avgwt = float(avgwt)/inp

    print("\n")
    print("Process\t  Burst Time\t  Waiting Time")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t\t" + str(f_wt[i]))
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
