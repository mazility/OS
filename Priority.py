def main():
    Priority()


def Priority():
    print("Enter the numbers of process: ")
    inp = int(input())
    proc, bt_sort1, bt_sort2, r_bt = [], [], [], []
    for i in range(0, inp):
        proc.insert(i, i)
        r_bt.append(0)

    print("\nEnter the burst time of the process with spaces: \n")
    bt = list(map(int, input().split()))
    for i in range(0, inp):
        bt_sort1.append(bt[i])
        bt_sort2.append(bt[i])

    print("\nEnter the priority of the process with spaces: \n")
    prio = list(map(int, input().split()))

    wt = []

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
                    temp = r_bt[i]
                    r_bt.pop(i)
                    r_bt.insert(i, temp + 1)
                    wt.insert(i, 1)
    print('wt',wt,'r_bt' , r_bt,'smallest_marker' , smallest_marker)

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
                temp = r_bt[j]
                r_bt[j] = r_bt[j+1]
                r_bt[j+1] = temp
    print(r_bt)
    wt.insert(0, 0)
    for i in range(1, inp):
        if r_bt[i] == 1:
            wt.insert(i, wt[i - 1] + bt[i - 1] + r_bt[i])
        else:
            wt.insert(i, wt[i - 1] + bt[i - 1])
    print(wt)
    avgwt = 0
    for i in range(0, inp):
        avgwt = avgwt + (wt[i] - proc[i])

    avgwt = float(avgwt) / inp

    print("\n")
    print("Process\t\t  Burst Time\t\t  Waiting Time\t\t Priority")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(wt[i]) + "\t\t\t" + str(prio[i]))
    print("Average Waiting time is: " + str(avgwt))


if __name__ == '__main__':
    main()
