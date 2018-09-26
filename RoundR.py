def main():
    RoundR()


def RoundR():
    print("Enter the numbers of process: ")
    inp = int(input())
    proc, proc2 = list(), list()
    for i in range(0, inp):
        proc.insert(i, i + 1)
        proc2.insert(i, i)
    print("\nEnter the burst time of the process with spaces: \n")
    bt = list(map(int, input().split()))
    print("\nEnter the time quantum value: ")
    tq = int(input())
    stopper, counter = 0, 0
    res_arr, res_temp, res_bt = list(), list(), list()
    res_c = list()
    t_bt, f_bt = [], []
    res_temp.append(0)
    for i in range(0, len(bt)):
        f_bt.append(0)
        res_bt.append(bt[i])
        res_c.append(0)
        res_arr.append(bt[i])
        t_bt.append(bt[i])
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
    round = 0
    for i in range(0, tq-1):
        for j in range(0, tq-1):
            if res_bt[j] > res_bt[j+1]:
                temp = res_bt[j]
                res_bt[j] = res_bt[j+1]
                res_bt[j+1] = temp
    round = res_bt[inp-1]
    r_round = round/inp
    if r_round > int(r_round):
        r_round += 1

    for i in range(0, len(t_bt)):
        for j in range(0, len(t_bt)):
            if t_bt[i] > tq:
                temp = t_bt[i]
                t_bt.pop(i)
                t_bt.insert(i, temp - tq)
                temp = f_bt[i]
                f_bt.pop(i)
                f_bt.insert(i, temp + 1 )

    for i in range(0, len(f_bt)):
        f_bt[i] *= 4

    for i in range(0, len(res_arr)):
        t = res_arr[i]
        res_arr.pop(i)
        res_arr.insert(i, t - proc2[i] - f_bt[i])
        avgwt += res_arr[i]

    avgwt = float(avgwt) / inp
    print("Process\t\t  Burst Time\t\t  Waiting Time")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(res_bt[i]) + "\t\t\t" + str(res_arr[i]))
    print("Average Waiting time is: " + str(avgwt))


if __name__ == '__main__':
    main()
