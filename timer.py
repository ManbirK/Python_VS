import time

seconds = input("Enter the time in number of seconds ")


def countdown_timer(seconds):
  
    mins = int(seconds / 60)
    secs = int(seconds % 60)
    timer = f'{mins} : {secs}'
    print(timer)
  

countdown_timer(int(seconds))