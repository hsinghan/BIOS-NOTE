import os


if __name__ == '__main__':
    BCU_path = os.getcwd() + '\\BiosConfigUtility64.exe'
    myCmd = "BiosConfigUtility64.exe /get:BCU_Setting.txt"
    os.system(myCmd)