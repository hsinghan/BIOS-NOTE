import os
import subprocess
import win32api
from tkinter import messagebox
import tkinter

def show_Message(msg):
    # hide main window
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Notification", msg)

def check_if_exist(path):
    return os.path.exists(path)


if __name__ == '__main__':
    # get file path
    BCU_path = os.getcwd() + '\\BiosConfigUtility64.exe'
    MPM_txt_path = os.getcwd() + '\\MPM_LOCK.txt'

    if False == check_if_exist(BCU_path):
        show_Message("BiosConfigUtility64.exe does not exist!!!")
    elif False == check_if_exist(MPM_txt_path):
        # TODO
        # Check txt file contents.
        show_Message("MPM_LOCK.txt does not exist!!!")
    else:
        # myCmd = "BiosConfigUtility64.exe /set:MPM_LOCK.txt"
        # os.system(myCmd)
        MsgBox = tkinter.messagebox.askquestion('Exit Application','Do you want to restart the computer now?',icon = 'warning')
        tkinter.withdraw()
        if MsgBox == 'Yes': #The return type of MsgBox is bool 
            print("Reboot now")
            #os.system("shutdown /r /t 3")
        else:
            print("Do not reboot now")
            show_Message('You need to restart the computer later for appling BIOS setting.')
