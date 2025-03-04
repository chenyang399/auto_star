from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
# 创建页面对象，并启动或接管浏览器
import pyautogui
import time
import shutil
import os
import win32api
import win32con
import pyautogui
import time
from faker import Faker
from DrissionPage.common import Actions
# 必须管理员权限运行！！！！
import random
# def main(i,page):

#     page.set.window.max()
#     page.get("https://chromewebstore.google.com/detail/%E6%AC%A7%E6%98%93-web3-%E9%92%B1%E5%8C%85/mcohilncbfahbmgdjkbpemcciiolgcge?hl=zh-CN")
#     page.set.window.show()
#     ele = page.ele('text=添加至 Chrome')
#     # page.handle_alert(accept=True,timeout=5)
#     page.set.window.show()
#     ele.click()
#     # 确认提示框并获取提示框文本
    
#     # 点击取消
#     time.sleep(5)
#     page.set.window.show()
#     try:
#         file_position = pyautogui.locateOnScreen(r"D:\2.png",confidence=0.6) 
#     except Exception as  e :
#         print("error in chrome "+str(i))
#         return
        
#     page.set.window.show()
#     position = pyautogui.center((file_position)) 
#     page.set.window.show()
#     pyautogui.click(position)

# def sign_in_okx(i,page):
#     tab = page.new_tab()
#     tab.get("chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/popup.html")
#     tab.ele("text=导入已有钱包").click()
#     tab.ele("text=助记词或私钥").click()
    
    


    
    
#     time.sleep(3)
#     tab.ele("text=确认").click()
    
    
#     eles = tab.eles("@class:okui-input-input")
#     # print(eles)

#     eles[0].input("che1061147781")
#     eles[1].input("che1061147781")
#     time.sleep(3)
#     tab.ele("text=确认").click()
    
    
#     tab.ele("text=暂时不用").click()
    
#     tab.ele("text:开启你的").click()
    
#     tab.close()
#     time.sleep(1)
    
    
#     # ele.child("tag:input").click()
#     # ele.child("tag:input").input("sadf")
#     # pyautogui.press('tab')
    
    
    
def auto_star(i,page,github_link):
    tab = page.new_tab()
    tab.get(github_link)
    ac = Actions(tab)
    time.sleep(1.8952)
    ele_star=tab.ele("text:Star").parent()
    ac.move_to(ele_or_loc=(1379,132),duration=0.85).click()
    tab.actions.move(300, 10)
    time.sleep(5.16516)
    tab.close()

    
    
    
    
# 运行代码部分
# 需要手动改定的部分
# 1. 需要点击的坐标，使用如下代码得到
# document.addEventListener('click', function(event) {  
#     const x = event.clientX;  // 获取相对于视口的X坐标  
#     const y = event.clientY;  // 获取相对于视口的Y坐标  
    
#     console.log(`X坐标: ${x}, Y坐标: ${y}`);  
# });
# 该代码需要先在页面右击鼠标，点击检查，然后点击console打开控制台页面，需要输入allow paste允许粘贴之后，复制代码运行，代码会报错，不用管
# 然后关闭刚刚的控制台，点击star，再打开控制台，会输出star位置的坐标，请你记录下来坐标，在auto_star函数的ac.move_to(ele_or_loc=(1379,132),duration=0.85).click()这一行把坐标修改。
# 2.修改github——link为自己的link
# 3. 修改chrome_path为自己的chrome path
# 注意！！！！不要放大页面，修改页面，保持默认设置

github_link="https://github.com/chenyang399/copy_chrome"
page_list=dict()

chrome_path = 'D:\chrome'
for i in range(3,100):
    
    data_path = chrome_path + "/"+str(i)
    co = ChromiumOptions().set_local_port(9550+i).set_user_data_path(data_path)
    page = ChromiumPage(co)
    # page_list[i]=page
    print("第"+str(i)+"个chrome")
    try:
        auto_star(i,page,github_link)
    except Exception as e:
        print(e)
        print("error in autostar()")
    page.close()
        
    
