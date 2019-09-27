import os
import subprocess
import win32api

def generate_setting_file():
    
    item_list = ['BIOSConfig 1.0\n',
                 'Product Name\n','\tHP ZBook 15c G7\n'
                 'Serial Number\n','\tCND84956VJ\n',
                 'SKU Number\n','\t123456#ABA\n',
                 'System Board CT Number\n','\tPXXXXA51UBNPVS\n',
                 'Feature Byte\n', '\t7R.3R\n',
                 'Build ID\n', '\t19WWMRAT6ae#SABA#DABA\n',
                 'Manufacturing Programming Mode\n', '\tUnlock\n','\t*Lock\n'
                 'HBMA Factory MAC Address\n', '\t12-34-56-78-90-AB\n',
                 'HBMA System MAC Address\n', '\t12-34-56-78-90-AB\n',
                 'Fast Boot\n','\tDisable\n','\t*Enable\n']

    # revise_list = []

    with open('MPM_LOCK.txt','w') as f1:
        f1.writelines(item_list)

    print(item_list)

    # for item in f1_text:
    #     if item in item_list:
    #         revise_list.append(item)
    #         for value in f1_text[f1_text.index(item)+1:] :
    #             if value[0] == '\t':
    #                 revise_list.append(value)
    #             else:
    #                 break
    # with open(des) as f2:
    #     f2_text = list(f2.readlines())



if __name__ == '__main__':

    # generate the setting file
    # generate_setting_file()
    # print("Hello world")

    # implement setting and remiove file
    myCmd = "BiosConfigUtility64.exe /set:MPM_LOCK.txt"
    os.system(myCmd)

    # working_path = os.getcwd()
    # print(working_path)
    # os.remove('setting_file.txt')
    print("Reboot....")
    os.system("shutdown /r /t 3")