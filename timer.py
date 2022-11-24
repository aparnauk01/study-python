import time

def count_Down(t):
    while t :
        min, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min,sec)
        print(timer, end= '\r')
        time.sleep(1)
        t=t-1
    

    


t = input("Enter the time: ")
count_Down(int(t))
