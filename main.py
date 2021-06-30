import time

print("Which is the one thing you forget the most ?")
help = input()

print("Do you need a reminder ? 0 -> no and 1 -> yes")
choice = int(input())

if (choice == 1):
    print("Next input will be to enter the number of hours,  minutes and second")
    print("Reminder is needed after how many hours ?")
    h = int(input())
    print("Reminder is needed after how many minutes ?")
    m = int(input())
    print("Reminder is needed after how many seconds ?")
    s = int(input())

    while(True):
        print(help)
        time.sleep(h*3600 + m*60 + s)
