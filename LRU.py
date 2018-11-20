#FIFO page replacement algorithm implementation in python
#Created By: Pannachet Lertananta
import random

arr = []
recently_arr = []

def main():
    global string, frame, page, pagefault
    string = int(input('\n Enter the size of reference string: '))
    frame = int(input('\n Enter the page frame size: '))
    print('\n Page frame size = ', frame)
    page = [None] * frame
    print(' ',page)
    randomNum()
    pageFault()

def randomNum():
    for i in range(0, string):
        arr.append(random.randint(0,9))
        recently_arr.append(arr[i])
    print('\n Random page reference string = ',arr ,'\n')

def pageFault():
    pagefault = 0

    #hit is when that particular reference string is present in the page so that will cause no change to the page
    hit = 0
    for i in range(0, frame):
        count = 0
        hitRecord = 0
        for j in range(1):
            curNum = i % frame
            if page[curNum] is None:
                print(' Added string to None value in array', i)
                page.pop(curNum)
                page.insert(curNum, arr[i])
                pagefault += 1
            print(' Current Page array', page, '\n')

    for i in range(0 + frame, string):
        count = 0
        r_count = 0
        t_count = 0
        hitRecord = 0
        temp = 0
        for j in range(1):
            curNum = i % frame

            while count != frame:
                if page[count] == arr[i]:
                    hit += 1
                    hitRecord = 1
                    count = frame
                    print(' Hit!')
                else:
                    count += 1

            if hitRecord == 1:
                while r_count != i - 1:
                    if recently_arr[r_count] == arr[i]:
                        recently_arr.pop(r_count)
                        r_count = i - 1
                    else:
                        r_count += 1

            if hitRecord == 0:
                temp = recently_arr[0]
                recently_arr.pop(0)
                if page[curNum] != arr[i]:
                    while t_count != frame:
                        if page[t_count] == temp:
                            page.pop(t_count)
                            page.insert(t_count, arr[i])
                            t_count = frame
                        else:
                            t_count += 1
                    pagefault += 1
                    print(' Pagefault!')
            print('', recently_arr,temp)
        print(' Current Page array', page, '\n')


    print('\n Page array = ',page ,'\n Page Faults = ', pagefault, '\n Hits = ', hit)

if __name__ == '__main__':
    main()
