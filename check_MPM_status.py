import os
# import subprocess
import win32api
from tkinter import messagebox
import tkinter

Unlock_Status = False
Lock_Status   = True

def show_Message(msg):
    # hide main window
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Notification",  msg)

def is_MPM_Lock(file_path):
    with open(file_path) as f:
        content = f.readlines()

    index = content.index('Manufacturing Programming Mode\n')

    result = "\tUnlock\n" in content[index+1]

    if result == Lock_Status:
        return Lock_Status
    else:
        return Unlock_Status


if __name__ == '__main__':
    # get file path
    BCU_path = os.getcwd() + '\\BiosConfigUtility64.exe'
    myCmd = "BiosConfigUtility64.exe /get:"BIOS_Setting.txt" "
    os.system(myCmd)
    MPM_txt_path = os.getcwd() + '\\BIOS_Setting.txt'

    if is_MPM_Lock(MPM_txt_path) :
        MPM_txt_path = os.getcwd() + '\\BIOS_Setting.txt'
        os.remove(MPM_txt_path)
        show_Message("The unit status in MPM Lock.")
    else:
        MPM_txt_path = os.getcwd() + '\\BIOS_Setting.txt'
        os.remove(MPM_txt_path)
        show_Message("The unit status in MPM UnLock.")


