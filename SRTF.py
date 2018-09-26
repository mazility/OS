def main():
    SRTF()


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

    avgwt = 0
    for i in range(0, len(bt)):
        avgwt += final_wt[i]
    avgwt = float(avgwt)/inp

    print("\n")
    print("Process\t\t  Burst Time\t\t  Waiting Time")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(f_wt[i]))
    print("Average Waiting time is: " + str(avgwt))


if __name__ == '__main__':
    main()
