import shutil
import os
import tkinter as tk

def Copy_Directory(src_path, des_path):
    src_Dir_list = os.listdir(src_path)
    #src_Dir_list.remove('HpPlatformPkg')
    print(src_Dir_list)
    for item in src_Dir_list:
        s = os.path.join(src_path, item)
        d = os.path.join(des_path, item)
        print('From {src} copy to {des}'.format(src=s ,des=d))
        shutil.copytree(s, d, symlinks=False)

def Delete_Directory(des_path):
    des_Dir_list = os.listdir(des_path)
    des_Dir_list.remove('HpPlatformPkg')
    print(des_Dir_list)
    # for item in des_Dir_list:
    #     d = os.path.join(des_path, item)
    #     shutil.rmtree(d)

def Initial_Windows():
    window = tk.Tk()
    window.title('Update Corebase')
    window.geometry('800x600')
    console = tk.Label(window, text='Welcome use the tool',font=('Arial',14), width=30, height=2)
    console.pack()
    window.mainloop()


if __name__ == '__main__':
    Initial_Windows()
    # Delete_Directory('C:\\TestFolder\\test2')
    #Copy_Directory('C:\\TestFolder\\00.13', 'C:\\TestFolder\\test2')
    print("hello, world")


