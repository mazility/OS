def main():
    print('\n\nPlease select the number of CPU scheduling options below\n1: FCFS\n2: Preemptive SJF(SRTF)\n3: Priority\n4: Round Robin')
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
        import FCFS
        FCFS.main()
    elif selection == 2:
        import SRTF
        SRTF.main()
    elif selection == 3:
        import Priority
        Priority.main()
    elif selection == 4:
        import RoundR
        RoundR.main()
    else:
        print("That's not an option!")
        main()


if __name__ == '__main__':
    main()
