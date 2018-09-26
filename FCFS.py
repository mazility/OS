def main():
    FCFS()


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
        else:
            wt.append(bt[i] + temp)
        avgwt += (wt[i] - (proc[i]-1))
    avgwt = float(avgwt)/inp
    print("\n")
    print("Process\t\t  Burst Time\t\t  Waiting Time")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(wt[i]))
    print("Average Waiting time is: " + str(avgwt))


if __name__ == '__main__':
    main()
