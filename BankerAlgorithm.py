import numpy as np

number_processes = int(input('Number of processes: '))
number_resources = int(input('Number of resources: '))

available_resources = [int(x) for x in input('Total system resources, with a space: ').split(' ')]

currently_allocated_resources = np.array(
    [[int(x) for x in input('Currently allocated resources ' + str(i + 1) + ' ? with a space:').split(' ')]
    for i in range(number_processes)])
maximum_resources = np.array([[int(x) for x in input('Maximum resources ' + str(i + 1) + ' ? with a space:').split(' ')] for i in
                       range(number_processes)])

total_available_resources = available_resources - np.sum(currently_allocated_resources, axis=0)

running = np.ones(number_processes)

while np.count_nonzero(running) > 0:
    at_least_one_allocated = False
    for p in range(number_processes):
        if running[p]:
            if all(i >= 0 for i in total_available_resources - (maximum_resources[p] - currently_allocated_resources[p])):
                at_least_one_allocated = True
                print(str(p) + ' is running')
                running[p] = 0
                total_available_resources += currently_allocated_resources[p]
    if not at_least_one_allocated:
        print('Status: Unsafe')
        exit()

print('Status: Safe')
