import os
# import subprocess
import win32api
from tkinter import messagebox
import linecache
import tkinter

def show_Message(msg):
    # hide main window
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Notification", msg)

def is_MPM_Lock(file_path):
    msg = linecache.getline(file_path, 108)
    print(msg)
    if '*Unlock' in msg:
        return False
    else:
        return True

if __name__ == '__main__':
    # get file path
    # BCU_path = os.getcwd() + '\\BiosConfigUtility64.exe'
    # myCmd = "BiosConfigUtility64.exe /get:"BIOS_Setting.txt"
    # os.system(myCmd)
    #MPM_txt_path = os.getcwd() + '\\BIOS_Setting.txt'

    if is_MPM_Lock('MU.txt') :
        show_Message("The unit is MPM Lock status!")
    else:
        show_Message("The unit is MPM UnLock status!")

    #MPM_txt_path = os.getcwd() + '\\BIOS_Setting.txt'
    #os.remove(MPM_txt_path)
