import shutil
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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
        self.geometry('600x400')
        self.wm_iconbitmap('coffee.ico')
        self.creatWidgets("Choose server package folder path", 0, 0)
        # self.labelFrame = ttk.LabelFrame(self, text = "Choose server package folder path")
        # self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        # self.button()
        
        self.creatWidgets("Choose release package folder path", 0, 20)
        # Prevent Window From Resizing
        #self.resizable(False, False)

        #self.configure(background = '#4D4D4D')
        #Set logo
        #self.wm_iconbitmap('file_name')

    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)

    def creatWidgets(self, string_text, x, y):
        self.label = Label(self, text = string_text, font=('Arial', 12), width=40,anchor=W,pady=5)
        self.label.grid(column = x, row = y)


if __name__ == '__main__':
    # create an windows to fetch the folder path
    root = Root()
    root.mainloop()

    # update files
    #Replace_all_files("C:\\github_repo\\BIOS-NOTE\\test1", "C:\\github_repo\\BIOS-NOTE\\test2")