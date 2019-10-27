import shutil
import os
from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog

Project_Code = ""    # Ex : S91
New_Version_Num = "" # Ex : 000200
Old_Version_Num = "" # Ex : 000100

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

class Root(Tk):
    """docstring for Root"""
    def __init__(self):
        super(Root, self).__init__()
        self.title('Update Release Package(Beta version)')
        self.geometry('800x600')
        self.wm_iconbitmap('coffee.ico')

        self.creatLabel('Choose release package folder path',x=0, y=0)
        self.labelFrame = ttk.LabelFrame(self, text = "")
        self.labelFrame.place(x=0, y=30)
        self.Browse_button()

        # self.creatLabel('Choose release package folder path',x=0, y=200)
        # self.labelFrame = ttk.LabelFrame(self, text = "")
        # self.labelFrame.place(x=0, y=230)
        # self.Browse_button()
        # Prevent Window From Resizing
        #self.resizable(False, False)

        #self.configure(background = '#4D4D4D')
        #Set logo
        #self.wm_iconbitmap('file_name')

    def Browse_button(self):
        self.button = tk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        #self.button.grid(column = 0, row = 1)
        self.button.grid(column = 0, row = 1)

    def fileDialog(self):
        self.filename = filedialog.askdirectory()
        self.label = ttk.Label(self.labelFrame, text = self.filename)
        self.label.grid(column = 1, row = 2)

    def creatLabel(self, string_text, x, y):
        # 說明： bg為背景，font為字型，width為長，height為高，
        # 這裡的長和高是字元的長和高，比如height=2,就是標籤有2個字元這麼高
        msg1 = tk.Label(self, text=string_text, font=('Arial', 13), width=0, height=2)
        msg1.place(x=x, y=y)

    def client_exit(self):
        exit()


if __name__ == '__main__':
    # create an windows to fetch the folder path
    root = Root()
    root.mainloop()

    # update files
    #Replace_all_files("C:\\github_repo\\BIOS-NOTE\\test1", "C:\\github_repo\\BIOS-NOTE\\test2")