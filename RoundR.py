def main():
    RoundR()


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
    print("Process\t\t  Burst Time\t\t  Waiting Time")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(res_bt[i]) + "\t\t\t" + str(res_arr[i]))
    print("Average Waiting time is: " + str(avgwt))


if __name__ == '__main__':
    main()
