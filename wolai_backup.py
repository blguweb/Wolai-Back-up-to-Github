from selenium import webdriver
import pyautogui
import glob
import os
from git import Repo
import pyperclip

def open_web():
    # #打开谷歌浏览器
    # driver = webdriver.Chrome()
    # #打开主页
    # driver.get('https://www.wolai.com/')
    app_dir = r'D:\wolaiNote\wolai.exe'
    os.startfile(app_dir)


def backup():
    pyautogui.PAUSE = 5
    pyautogui.FAILSAFE = True      # 启用自动防故障功能
    width,height = pyautogui.size()   # 屏幕的宽度和高度
    pyautogui.position()        # 鼠标当前位置
    pyautogui.moveTo(80,167,duration=0.25)  # 点击自己想要保存的文件夹
    pyautogui.click(80,167)           
    pyautogui.PAUSE = 1
    print("select what to back up")

    pyautogui.moveTo(1893,20,duration=0.25)  # 打开右侧栏，三个点
    pyautogui.click(1893,20)           
    pyautogui.PAUSE = 1
    print("open the column")
    
    pyautogui.moveTo(1707,446,duration=0.25)  # 点击导出页面
    pyautogui.click(1707,446)           
    pyautogui.PAUSE = 1
    print("click to export")

    pyautogui.moveTo(863,470,duration=0.25)  #点击MD格式
    pyautogui.click(863,470)           
    pyautogui.PAUSE = 1
    print("select MD format")
    
    pyautogui.moveTo(1013,626,duration=0.25)
    pyautogui.click(1013,626)           # 点击导出
    pyautogui.PAUSE = 8
    print("start to export")
    
    pyautogui.moveTo(1122,502,duration=0.25)
    pyautogui.click(1122,502)           # 点击更改目录
    pyautogui.PAUSE = 1
    print("click to change path")

    pyautogui.moveTo(1164,265,duration=0.25)
    pyautogui.click(1164,265)           # 点击目录路径行
    pyautogui.PAUSE = 1
    print("click where to change")
    
    # pyperclip.copy('D:\wolai')
    # pyperclip.paste()
    pyautogui.typewrite('D:\wolai\Wolai_Backup',0.25) #输入自己想要的路径
    pyautogui.typewrite(['enter']) 
    pyautogui.moveTo(1521,716,duration=0.25)
    pyautogui.click(1521,716)           # 点击保存
    print("changed path")
    pyautogui.moveTo(1020,533,duration=0.25)
    pyautogui.click(1020,533)           # 文件已经存在确定覆盖

    pyautogui.moveTo(956,612,duration=0.25)
    pyautogui.click(956,612)           # 点击开始下载
    pyautogui.PAUSE = 1
    print("have downloaded")
    


# def unzip_files():
#     path = r'D:\wolai\Wolai_Backup'
#     file_lst = glob.glob(path + '/*')
#     # 列表推导式
#     filename_lst = [os.path.basename(i) for i in file_lst]
#     print(filename_lst)
#     # 如果有文件夹那么就需要进一步的点击操作
#     for filename in filename_lst:
#         if '.' in filename:
#             suffix = filename.split('.')[-1]
#             if suffix == 'gz':
#                 new_filename = ungz(filename)
#                 os.remove(filename)
#                 if new_filename.split('.')[-1] == 'tar':
#                     untar(new_filename)
#                     os.remove(new_filename)
#             if suffix == 'tar':
#                 untar(filename)
#                 os.remove(filename)
#             if suffix == 'zip':
#                 unzip(filename)
#                 os.remove(filename)
#             if suffix == 'rar':
#                 unrar(filename)
#                 os.remove(filename)


# def unzip(filename):
#     zip_file = zipfile.ZipFile(filename)
#     if not os.path.isdir(filename + "_dir"):
#         os.mkdir(filename + "_dir")
#     for names in zip_file.namelist():
#         zip_file.extract(names, filename + "_dir/")

def git_push():
    dirfile = os.path.abspath('./') # code的文件位置，我默认将其存放在根目录下
    print("dir",dirfile)
    repo = Repo(dirfile)

    g = repo.git
    g.add("--all")
    g.commit("-m auto update")
    g.push()
    print("Successful push!")


if __name__=='__main__':
    open_web()
    backup()
    git_push()
