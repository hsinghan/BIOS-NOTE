import shutil
import os
import tkinter as tk
from os.path import basename

def Copy_all_files(src_path, des_path):
    File_list = os.listdir(des_path)
    print("Destination path : " + src_path)
    for item in File_list:
        file_full_path = os.path.join(des_path, item)
        print('File {file_name} copy to {des_folder_path}'.format(file_name=item ,des_folder_path=src_path))
        try:
            shutil.copy(file_full_path, src_path)
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

def Replace_all_files(old, new):
    """
    Delet all files under old path, 
    and copy all files from new to old.
    """
    if os.path.isdir(old) and os.path.isdir(new):
        print("Both of paths exits")
        Delete_all_files(old)
        Copy_all_files(old, new)
    else:
        print("Unvalid dir path")

# def Initial_Windows():
#     window = tk.Tk()
#     window.title('Update Release Package')
#     window.geometry('800x600')
#     console = tk.Label(window, text='Welcome use the tool',font=('Arial',14), width=30, height=2)
#     console.pack()
#     window.mainloop()

if __name__ == '__main__':
    # create an windows to fetch the folder path
    # Initial_Windows()
    # update files
    Replace_all_files("C:\\github_repo\\BIOS-NOTE\\test1", "C:\\github_repo\\BIOS-NOTE\\test2")

