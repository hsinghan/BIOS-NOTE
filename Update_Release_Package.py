import shutil
import os
#from tkinter import * 
import re
import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
from tkinter import messagebox

New_Version_Num = "" # Ex : S91_000200 
Old_Version_Num = "" # Ex : S91_000100 
 
New_Server_Package_path = "" 
Release_Package_path = "" 

def Copy_all_files(src_path, des_path):
    File_list = os.listdir(src_path)
    print("Destination path : " + des_path)
    for item in File_list:
        file_full_path = os.path.join(src_path, item)
        print('File {file_name} copy to {des_folder_path}'.format(file_name=item ,des_folder_path=des_path))
        try:
            shutil.copy2(file_full_path, des_path)
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
    Delete all files under package_path path, 
    and copy all files from server_package_path to package_path.
    """
    if os.path.isdir(package_path) and os.path.isdir(server_package_path):
        print("Both of paths exits")
        Delete_all_files(package_path)
        Copy_all_files(server_package_path, package_path)
    else:
        print("Unvalid dir path")


def Replace_one_file(old_file_path, new_file_path):
    if os.path.isfile(old_file_path) and os.path.isfile(new_file_path):
        os.remove(old_file_path)
        shutil.copy2(new_file_path, Path(old_file_path).parents[0])
    else:
        print("Unvalid dir path")


def check_path_and_version():
    if New_Version_Num == "":
        show_Message("The New BIOS Version can not be empty")
        # TODO 
        # Check if the input value is valid
        return

    if Old_Version_Num == "":
        show_Message("The Old BIOS Version can not be empty")
        return

def Update_Capsule_folder(Release_Package_path, New_Server_Package_path):
    src_list = ['\\Capsule\\Windows\\Combined FW Image (BIOS, ME, PD)',
                '\\Capsule\\Linux\\Combined FW Image (BIOS, ME, PD)',
                '\\Capsule\\Windows\\Thunderbolt',
                '\\Capsule\\Linux\\Thunderbolt'] 

    des_list = ['\\Combined\\WU',
                '\\Combined\\Linux',
                '\\TBT',
                '\\TBT']    

    for src_item, des_item in zip(src_list, des_list):
        Replace_all_files(Release_Package_path + src_item, New_Server_Package_path + des_item)


def Update_HPFWUPDREC_folder(Release_Package_path, New_Server_Package_path):
    Replace_one_file(Release_Package_path +'\\HPFWUPDREC\\' + Old_Version_Num + '.bin',
                     New_Server_Package_path +'\\Combined\\FUR\\' + New_Version_Num + '.bin')

    Replace_one_file(Release_Package_path +'\\HPFWUPDREC\\' + Old_Version_Num + '.inf', 
                     New_Server_Package_path +'\\Combined\\FUR\\' + New_Version_Num + '.inf' )

    Replace_one_file(Release_Package_path +'\\HPFWUPDREC\\' + 'CombinBuild.Log',
                     New_Server_Package_path +'\\Combined\\FUR\\' + 'CombinBuild.Log')


def Update_FPTW_folder(Release_Package_path, New_Server_Package_path):
    Replace_one_file(Release_Package_path +'\\FPTW\\' + Old_Version_Num + '_32.bin',
                     New_Server_Package_path +'\\' + New_Version_Num + '_32.bin')

    revise_batch_file(Release_Package_path +'\\FPTW\\Update32.bat', 
                      Old_Version_Num + '_32.bin',
                      New_Version_Num + '_32.bin')

    revise_batch_file(Release_Package_path +'\\FPTW\\Update64.bat', 
                      Old_Version_Num + '_32.bin',
                      New_Version_Num + '_32.bin')


def Update_GLOBAL_folder(Release_Package_path, New_Server_Package_path):
    Replace_one_file(Release_Package_path +'\\GLOBAL\\BIOS\\' + Old_Version_Num + '_32.bin',
                     New_Server_Package_path +'\\' + New_Version_Num + '_32.bin' )

    Replace_one_file(Release_Package_path +'\\GLOBAL\\BIOS\\' + Old_Version_Num + '.bin',
                     New_Server_Package_path +'\\' + New_Version_Num + '.bin')


def Start_Update_Package():
    global New_Version_Num, Old_Version_Num
    global New_Server_Package_path, Release_Package_path

    check_path_and_version()

    # Update BUFF folder
    Replace_one_file(Release_Package_path +'\\BUFF\\' + Old_Version_Num + '_32.bin',
                     New_Server_Package_path +'\\' + New_Version_Num + '_32.bin')

    # Update Capsule folder
    Update_Capsule_folder(Release_Package_path, New_Server_Package_path)

    # Update FPTW folder
    Update_FPTW_folder(Release_Package_path, New_Server_Package_path)

    # Update GLOBAL folder
    Update_GLOBAL_folder(Release_Package_path, New_Server_Package_path)

    # Update FUR folder
    Update_HPFWUPDREC_folder(Release_Package_path, New_Server_Package_path)

    show_Message("Update Completed!!!")


def revise_batch_file(file, old_str, new_str):
     """
     replace string in file.
     :param file name
     :param old_str
     :param new_str
     :return:
     """
     text_data = ""
     with open(file, "r", encoding="utf-8") as f:
         for line in f:
             if old_str in line:
                  line = line.replace(old_str,new_str)
             text_data += line
     
     with open(file,"w",encoding="utf-8") as f:
         f.write(text_data)
 

def show_Message(msg):
    # hide main window
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Notification", msg)


def fileDialog():
    global New_Server_Package_path, New_Version_Num
    app_windows.filename = filedialog.askdirectory()
    app_windows.label = ttk.Label(app_windows.labelFrame, text = app_windows.filename)
    app_windows.label.grid(column = 1, row = 1)
    New_Server_Package_path = str(Path(app_windows.filename))
    New_Version_Num = get_Version_Num(New_Server_Package_path)
    version_text_field = tk.Label(app_windows, text = New_Version_Num, font=('Arial', 11), width=10, height=2)
    version_text_field.place(x=115, y=75)

def get_Version_Num(path):
    file_list = os.listdir(path)
    rx = r'^[A-Z][0-9][0-9]_[A-Za-z0-9]{6}\\*'
    for item in file_list:
        if re.search(rx, item):
           print(item.split('.')[0])
           return item.split('.')[0]
    else:
        print('Not found')


def Browse_button(app_windows, x, y):
    app_windows.button = tk.Button(app_windows.labelFrame, text = "Browse A Folder",command = fileDialog)
    app_windows.button.grid(column = x, row = y)

def fileDialog2():
    global Release_Package_path, Old_Version_Num
    app_windows.filename = filedialog.askdirectory()
    app_windows.label2 = ttk.Label(app_windows.labelFrame2, text = app_windows.filename)
    app_windows.label2.grid(column = 1, row = 8)
    Release_Package_path = str(Path(app_windows.filename))
    Old_Version_Num = get_Version_Num(Release_Package_path + '\\HPFWUPDREC')
    version_text_field = tk.Label(app_windows, text = Old_Version_Num, font=('Arial', 11), width=10, height=2)
    version_text_field.place(x=115, y=193)


def Browse_button2(app_windows, x, y):
    app_windows.button2 = tk.Button(app_windows.labelFrame2, text = "Browse A Folder",command = fileDialog2)
    app_windows.button2.grid(column = x, row = y)

def client_exit():
    exit()


if __name__ == '__main__':
    # create an windows to fetch the folder path

    app_windows = tk.Tk() 

    app_windows.title('Update Release Package(Beta version)')
    app_windows.geometry('800x300')
    app_windows.wm_iconbitmap('coffee.ico')
    # Prevent Window From Resizing
    app_windows.resizable(False, False)

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

    msg1 = tk.Label(app_windows, text='New BIOS Version:', font=('Arial', 10), width=0, height=2)
    msg1.place(x=0, y=75)
    
# ------------------------------------------------------------------------------
    msg1 = tk.Label(app_windows, text='Choose Release package folder path', font=('Arial', 12), width=0, height=2)
    msg1.place(x=0, y=120)

    app_windows.labelFrame2 = ttk.LabelFrame(app_windows, text = "")
    app_windows.labelFrame2.place(x=0, y=150)
    Browse_button2(app_windows,0, 8)

    msg1 = tk.Label(app_windows, text='Old BIOS Version:', font=('Arial', 10), width=0, height=2)
    msg1.place(x=0, y=193)


# ------------------------------------------------------------------------------
    UpdateButton = tk.Button(app_windows, text = 'Update', font=('Arial', 13), command=Start_Update_Package)
    UpdateButton.place(x=630, y=250)

    ExitButton = tk.Button(app_windows, text = 'Exit', font=('Arial', 13), command=client_exit)
    ExitButton.place(x=730, y=250)

    app_windows.mainloop()
    # update files
    #Replace_all_files("C:\\github_repo\\BIOS-NOTE\\test1", "C:\\github_repo\\BIOS-NOTE\\test2")
    # resultButton = tk.Button(app_windows, text = 'Get Result', command=callbackFunc)
    # resultButton.place(x=0, y=300)

    # resultString = tk.StringVar()
    # resultLabel = tk.Label(app_windows, textvariable=resultString)
    # resultLabel.place(x=100, y=300)
    