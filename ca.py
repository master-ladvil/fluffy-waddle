from win32gui import GetWindowText, GetForegroundWindow
import time
import subprocess
import ctypes  # An included library with Python install.   

time.sleep(6)
process = "feedback"


while(True):

    current_process = (GetWindowText(GetForegroundWindow()))

    if(process != current_process):
        
        ctypes.windll.user32.MessageBoxW(0, "Navigation Detected", "alert", 1)  
        time.sleep(3)

    

    