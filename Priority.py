def main():
    Priority()


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

    avgwt = 0
    for i in range(0, len(proc)):
        avgwt = avgwt + wt[i]

    avgwt = float(avgwt) / inp

    print("\n")
    print("Process\t\t  Burst Time\t\t  Waiting Time\t\t Priority")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(wt[i]) + "\t\t\t" + str(prio[i]))
    print("Average Waiting time is: " + str(avgwt))


if __name__ == '__main__':
    main()
