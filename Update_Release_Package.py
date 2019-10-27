import shutil
import os
from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path

Project_Code    = "" # Ex : S91
New_Version_Num = "" # Ex : 000200
Old_Version_Num = "" # Ex : 000100
New_Server_Package_path = ""
Release_Package_path = ""

server_package_path_list = ['\\Combined\\FUR', 
                            '\\Combined\\WU', 
                            '\\ME', 
                            '\\TBT' ]

Release_Package_path_list = ['\\BUFF', 
                             '\\Capsule\\Windows\\Combined FW Image (BIOS, ME, PD)',
                             '\\Capsule\\Windows\\Thunderbolt',
                             '\\FPTW',
                             '\\GLOBAL\\BIOS',
                             '\\HPFWUPDREC',
                             '\\XML']

def Copy_all_files(src_path, des_path):
    File_list = os.listdir(src_path)
    print("Destination path : " + des_path)
    for item in File_list:
        file_full_path = os.path.join(src_path, item)
        print('File {file_name} copy to {des_folder_path}'.format(file_name=item ,des_folder_path=des_path))
        try:
            shutil.copy(file_full_path, des_path)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())

def Delete_all_files(path):
    input_path = os.listdir(path)
    print(input_path)
    for item in input_path:
        file_path = os.path.join(path, item)
        print(file_path)
        os.remove(file_path)

def Replace_all_files(package_path, server_package_path):
    """
    Delet all files under package_path path, 
    and copy all files from server_package_path to package_path.
    """
    if os.path.isdir(package_path) and os.path.isdir(server_package_path):
        print("Both of paths exits")
        Delete_all_files(package_path)
        Copy_all_files(server_package_path, package_path, )
    else:
        print("Unvalid dir path")


def Start_Update_Package():
    # data_folder = Path("source_data/text_files/")
    # file_to_open = data_folder / "raw_data.txt"
    # f = open(file_to_open)
    # Update BUFF
    # Update Capsule
    # Update FPTW
    # Update GLOBAL
    # Update FUR

def callbackFunc():
    resultString.set("{} - {}".format(firstlandString.get(),SecondlandString.get()))
    print(resultString)

def fileDialog():
    app_windows.filename = filedialog.askdirectory()
    app_windows.label = ttk.Label(app_windows.labelFrame, text = app_windows.filename)
    app_windows.label.grid(column = 1, row = 1)
    New_Server_Package_path = Path(app_windows.filename)
    print(New_Server_Package_path)

def Browse_button(app_windows, x, y):
    app_windows.button = tk.Button(app_windows.labelFrame, text = "Browse A Folder",command = fileDialog)
    app_windows.button.grid(column = x, row = y)

def fileDialog2():
    app_windows.filename = filedialog.askdirectory()
    app_windows.label2 = ttk.Label(app_windows.labelFrame2, text = app_windows.filename)
    app_windows.label2.grid(column = 1, row = 8)
    Release_Package_path = Path(app_windows.filename)
    print(Release_Package_path)

def Browse_button2(app_windows, x, y):
    app_windows.button2 = tk.Button(app_windows.labelFrame2, text = "Browse A Folder",command = fileDialog2)
    app_windows.button2.grid(column = x, row = y)

def client_exit():
    exit()

if __name__ == '__main__':
    # create an windows to fetch the folder path

    app_windows = tk.Tk() 

    app_windows.title('Update Release Package(Beta version)')
    app_windows.geometry('600x400')
    app_windows.wm_iconbitmap('coffee.ico')
    # Prevent Window From Resizing
    #app_windows.resizable(False, False)

    #app_windows.configure(background = '#4D4D4D')
    #Set logo
    #app_windows.wm_iconbitmap('file_name')

    msg1 = tk.Label(app_windows, text='Choose Server package folder path', font=('Arial', 12), width=0, height=2)
    msg1.place(x=0, y=0)

    app_windows.labelFrame = ttk.LabelFrame(app_windows, text = "")
    app_windows.labelFrame.place(x=0, y=30)
    # app_windows.button = tk.Button(app_windows.labelFrame, text = "Browse A Folder",command = app_windows.fileDialog)
    # app_windows.button.grid(column = 0, row = 1)
    Browse_button(app_windows,0, 1)

    msg1 = tk.Label(app_windows, text='Enter New BIOS Version:', font=('Arial', 11), width=0, height=2)
    msg1.place(x=0, y=75)

    firstlandString = tk.StringVar()
    #firstlandString.set('S91_000800')
    version_text_field = tk.Entry(app_windows, show=None, font=('Arial', 11), width=20, textvariable=firstlandString)  # 顯示成明文形式
    version_text_field.place(x=170, y=85)
    New_Version_Num = firstlandString.get()
# ------------------------------------------------------------------------------
    msg1 = tk.Label(app_windows, text='Choose Release package folder path', font=('Arial', 12), width=0, height=2)
    msg1.place(x=0, y=110)

    app_windows.labelFrame2 = ttk.LabelFrame(app_windows, text = "")
    app_windows.labelFrame2.place(x=0, y=140)
    Browse_button2(app_windows,0, 8)

    msg1 = tk.Label(app_windows, text='Enter Old BIOS Version:', font=('Arial', 11), width=0, height=2)
    msg1.place(x=0, y=185)

    SecondlandString = tk.StringVar()
    #SecondlandString.set('S91_000800')
    version_text_field = tk.Entry(app_windows, show=None, font=('Arial', 12), width=20, textvariable=SecondlandString)  # 顯示成明文形式
    version_text_field.place(x=170, y=195)
    Old_Version_Num = SecondlandString.get()

# ------------------------------------------------------------------------------
    UpdateButton = tk.Button(app_windows, text = 'Update', font=('Arial', 13), command=Start_Update_Package)
    UpdateButton.place(x=160, y=250)

    ExitButton = tk.Button(app_windows, text = 'Exit', font=('Arial', 13), command=client_exit)
    ExitButton.place(x=260, y=250)

    app_windows.mainloop()
    # update files
    #Replace_all_files("C:\\github_repo\\BIOS-NOTE\\test1", "C:\\github_repo\\BIOS-NOTE\\test2")
    # resultButton = tk.Button(app_windows, text = 'Get Result', command=callbackFunc)
    # resultButton.place(x=0, y=300)

    # resultString = tk.StringVar()
    # resultLabel = tk.Label(app_windows, textvariable=resultString)
    # resultLabel.place(x=100, y=300)
    