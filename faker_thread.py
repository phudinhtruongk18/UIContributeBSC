import os
from threading import Thread
import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException as NotFoundNtn

from helper import get_num_of_holder
from datetime import datetime

options = webdriver.ChromeOptions()
desired_cap = {
    'browserName': 'iPhone',
    'device': 'iPhone 11',
    'realMobile': 'true',
    'os_version': '14.0',
    'deviceOrientation': 'landscape'
}
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("window-size=950,900")
options.add_argument('headless')

url_father = "https://bscscan.com/token/"

class TheOne(Thread):
    def __init__(self, address,ui,timer):
        super().__init__()
        self.timer = timer  
        self.link = url_father + address
        self.ui = ui

        self.google = webdriver.Chrome(options=options, executable_path="./DATA/chromedriver.exe")
        self.google.set_page_load_timeout(40)
    
        self.google.set_window_position(900, 50, windowHandle='current')
        self.is_alive_mine = True

    def run(self):
        print("Hello world!")
        while self.is_alive_mine:
            try:
                self.google.get(self.link)
                self.waiting_for_love()
            except Exception as e:
                print("Line 39 FAKER THREAD ERROR: ", e)
                print(e)
            print("======================")
            holders, name =  self.get_holders()
            x = datetime.now()
            date = x.strftime("%Hh%M")
            self.ui.update_ui(holders, name, date)
            print(holders)
            print(name)
            print(date)
            print("======================")
            for _ in range(self.timer):
                if self.is_alive_mine:
                    time.sleep(1)
                else:
                    break
        self.close_google()
        self.ui.stop_scaner()

    def get_holders(self):
        try:
            holders = self.google.find_element_by_xpath("//*[@id=\"ContentPlaceHolder1_tr_tokenHolders\"]/div/div[2]/div/div")
            holders_text = holders.text
            holder_num = get_num_of_holder(holders_text)
        except Exception as e:
            holder_num = "Not Found"

        try:
            name = self.google.find_element_by_xpath("//*[@id=\"content\"]/div[1]/div/div[1]/h1/div/span")
            name_text = name.text
        except Exception as e:
            name_text = "Not Found"

        return holder_num, name_text

    def waiting_for_love(self):
        while True:
            page_state = self.google.execute_script('return document.readyState;')
            print(page_state)
            time.sleep(.1)
            if page_state == 'complete':
                break

    def close_google(self):
        self.is_alive_mine = False
        try:
            self.theone.close_google()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # address = ["0xf0a8ecbce8caadb7a07d1fcd0f87ae1bd688df43","0x8c5921a9563e6d5dda95cb46b572bb1cc9b04a27",
    # "0xf66a8a197d5cb0e2799d79be115208899332a0ba","0xa0c8c80ed6b7f09f885e826386440b2349f0da7e",
    # "0xb9b280f4277b49d59ac15283b6ae00a90aac5415","0x9d52414c4cc1fb8e7864a9b59495f430f8e5de44"]
    address = ["0xf0a8ecbce8caadb7a07d1fcd0f87ae1bd688df43"]
    list_thread = []
    for temp in address:
        thread = TheOne(temp)
        list_thread.append(thread)
        thread.start()

    for temp in list_thread:
        thread.join()

