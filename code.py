import pynput
from pynput.keyboard import Key,Controller
import time
def mainProgram(refresh_interval,stopper):
        keyboard=Controller()
        for _ in range(0,stopper):
            time.sleep(refresh_interval)
            keyboard.press(Key.f5)
            keyboard.release(Key.f5)
           
           
            
        return()
        
if __name__=='__main__': 
    refresh_interval=int(input("Enter the time interval for refreshing in seconds : "))
    choose_run=input("Click 'A' to give number of times you want to refresh/ Click any key for default setting.")
    
    if choose_run=="A" or choose_run=="a":
        stopper= int(input("Enter for how many times do you want to refresh: "))
        mainProgram(refresh_interval,stopper)
    else:      
        for _ in range(0,4):
                mainProgram(refresh_interval,5)
               
                Quit=input("Select 'Y' to quit the process/and any key to elsewise: ")
                if Quit=="Y" or Quit =="y":
                    break
                else:
                    mainProgram(refresh_interval,5)
