import shutil
import os
import tkinter as tk
from os.path import basename

def Copy_all_files(old_path, new_path):
    new_files = os.listdir(new_path)

    print(new_path)
    for item in new_files:
        d = os.path.join(new_path)
        print('File {src} copy to {des}'.format(src=item ,des=d))
        # try:
        #     shutil.copy(source, target)
        # except IOError as e:
        #     print("Unable to copy file. %s" % e)
        # except:
        #     print("Unexpected error:", sys.exc_info())


        

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
        #Delete_all_files(old)
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

def displayFileStats(filename):
    file_stats = os.stat(basename(filename))
    print('\tMode    :', file_stats.st_mode)
    print('\tCreated :', time.ctime(file_stats.st_ctime))
    print('\tAccessed:', time.ctime(file_stats.st_atime))
    print('\tModified:', time.ctime(file_stats.st_mtime))

if __name__ == '__main__':
    # create an windows to fetch the folder path
    # Initial_Windows()
    # update files
    Replace_all_files("C:\\github_repo\\BIOS-NOTE\\test1", "C:\\github_repo\\BIOS-NOTE\\test2")

