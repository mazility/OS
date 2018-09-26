def main():
    Priority()

def Priority():
    print("Enter the numbers of process: ")
    inp = int(input())
    proc, graph_proc, graph_arr, graph_prio, graph_bt, tgraph, pgraph, prgraph, wt = [], [], [], [], [], [], [], [], []

    print("\nEnter the burst time of the process with spaces: \n")
    bt = list(map(int, input().split()))

    print("\nEnter the priority of the process with spaces: \n")
    prio = list(map(int, input().split()))
    for i in range(inp):
        proc.append(i + 1)
        graph_arr.append(0)
        graph_prio.append(prio[i])
        graph_bt.append(bt[i])
        graph_proc.append(proc[i])
        
    sort(bt, prio, proc)
    smallest_marker = proc[0]
    graph(graph_bt, graph_prio, graph_proc,smallest_marker, graph_arr)
    gsort(graph_bt, graph_prio, graph_proc, graph_arr)

    for i in range(inp):
        tgraph.append(graph_arr[i])
        pgraph.append(graph_proc[i])
        prgraph.append(graph_arr[i])

    res = 0
    graph_psort(graph_proc, tgraph)
    graph_sort(graph_prio, graph_arr)
    waitingTime(graph_bt, graph_arr, wt, tgraph, proc, prgraph, res)

    for i in range(0, inp):
        temp = wt[i]
        wt.pop(i)
        wt.insert(i, temp - graph_arr[i])

    csort(wt, prio, proc, bt)

    avgwt = 0
    for i in range(0, inp):
        avgwt = avgwt + (wt[i] - (graph_proc[i] - 1))

    avgwt = float(avgwt) / inp

    print("\n")
    print("Process\t\t  Burst Time\t\t  Waiting Time\t\t Priority")
    for i in range(0, inp):
        print(str(proc[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(wt[i]) + "\t\t\t" + str(prio[i]))
    print("Average Waiting time is: " + str(avgwt))

def sort(ip, prio, proc):
    for i in range(0, len(ip) - 1):
        for j in range(0, len(ip) - i - 1):
            if prio[j] > prio[j+1]:
                temp = prio[j]
                prio[j] = prio[j+1]
                prio[j+1] = temp
                temp = ip[j]
                ip[j] = ip[j+1]
                ip[j+1] = temp
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp

def csort(ip, prio, proc, bt):
    for i in range(0, len(ip) - 1):
        for j in range(0, len(ip) - i - 1):
            if proc[j] > proc[j+1]:
                temp = prio[j]
                prio[j] = prio[j+1]
                prio[j+1] = temp
                temp = ip[j]
                ip[j] = ip[j+1]
                ip[j+1] = temp
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp
                temp = bt[j]
                bt[j] = bt[j+1]
                bt[j+1] = temp

def gsort(ip, prio, proc, graph):
    for i in range(0, len(ip) - 1):
        for j in range(0, len(ip)-1):
            if prio[j] > prio[j+1]:
                temp = prio[j]
                prio[j] = prio[j+1]
                prio[j+1] = temp
                temp = ip[j]
                ip[j] = ip[j+1]
                ip[j+1] = temp
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp
                temp = graph[j]
                graph[j] = graph[j+1]
                graph[j+1] = temp


def graph(ip, prio, proc, smallest_marker, graph_arr):
    for i in range(0, len(ip)-1):
        if proc[i] == smallest_marker or proc[i+1] == smallest_marker :
            break
        for j in range(i, len(ip) - 1):
            if prio[j] < prio[j+1] and proc[j] != smallest_marker and proc[j+1] != smallest_marker:
                temp = graph_arr[j]
                graph_arr.pop(j)
                graph_arr.insert(j, temp + 1)
                temp = prio[j]
                prio[j] = prio[j+1]
                prio[j+1] = temp
                temp = ip[j]
                ip[j] = ip[j+1]
                ip[j+1] = temp
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp
                temp = graph_arr[j]
                graph_arr[j] = graph_arr[j+1]
                graph_arr[j+1] = temp
            elif prio[j] > prio[j+1] and proc[j] != smallest_marker and proc[j+1] != smallest_marker:
                if graph_arr[j+1] > 0:
                    temp = graph_arr[j+1]
                    graph_arr.pop(j+1)
                    graph_arr.insert(j+1, temp + 1)
                else:
                    temp = graph_arr[j]
                    graph_arr.pop(j)
                    graph_arr.insert(j, temp + 1)

def re_sort(ip, prio, proc, graph):
    for i in range(0, len(ip) - 1):
        for j in range(0, len(ip) - i - 1):
            if proc[j] > proc[j+1]:
                temp = prio[j]
                prio[j] = prio[j+1]
                prio[j+1] = temp
                temp = ip[j]
                ip[j] = ip[j+1]
                ip[j+1] = temp
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp
                temp = graph[j]
                graph[j] = graph[j+1]
                graph[j+1] = temp

def graph_sort(prio, graph):
    for i in range(0, len(prio) - 1):
        for j in range(0, len(prio) - i - 1):
            if prio[j] < prio[j+1]:
                temp = prio[j]
                prio[j] = prio[j+1]
                prio[j+1] = temp
                temp = graph[j]
                graph[j] = graph[j+1]
                graph[j+1] = temp

def graph_psort(proc, graph):
    for i in range(0, len(proc) - 1):
        for j in range(0, len(proc) - i - 1):
            if proc[j] > proc[j+1]:
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp
                temp = graph[j]
                graph[j] = graph[j+1]
                graph[j+1] = temp


def waitingTime(bt, graph, wt, tgraph, proc, prio, res):
    for i in range(0, len(bt) - 1):
        if graph[i] == 0 and i > 0:
            graph.pop(i)
        else:
            wt.append(graph[i])

    temp_bt, temp_proc, temp_prio = [], [], []
    for i in range(0, len(bt)):
        temp_bt.append(bt[i])
        temp_proc.append(proc[i])
        temp_prio.append(prio[i])

    for i in range(0, len(bt) - 1):
        temp = temp_bt[i]
        temp_bt.pop(i)
        temp_bt.insert(i, temp - temp_prio[i])

    for i in range(0, len(bt) - 1):
        wt.append(temp_bt[i])

    wtLen = 0
    for i in range(0, len(bt) - 1):
        if temp_prio[i] > 0:
            wtLen += 1

    for i in range(1, len(bt) + wtLen):
        temp = wt[i]
        wt.pop(i)
        wt.insert(i, temp + wt[i-1])

    for i in range(0, wtLen):
        wt.pop(0)

    for i in range(0, len(bt)):
        res += wt[i]


if __name__ == '__main__':
    main()
