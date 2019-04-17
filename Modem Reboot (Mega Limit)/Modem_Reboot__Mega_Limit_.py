
from selenium import webdriver
import time
import os

def modemreboot():
    driver_path = "C:\\Users\\valid\\Downloads\\chromedriver\\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.get("http://192.168.1.1/#__restart.htm")
    time.sleep(3)

    kullanici = browser.find_element_by_id("userName")
    sifre = browser.find_element_by_id("pcPassword")
    oturumac = browser.find_element_by_id("loginBtn")

    kullanici.send_keys("admin")
    sifre.send_keys("2EY*12em-")

    oturumac.click()

    time.sleep(2)
    button_reboot = browser.find_element_by_id("button_reboot") #button_reboot idini bul ve değişken ata
    button_reboot.click() #button_reboot'a tıkla

    time.sleep(1)
    alert = browser.switch_to.alert #tarayıcıda uyarı var
    time.sleep(1)
    alert.accept() # uyarıyı kabul et
    time.sleep(20)
    browser.quit() #tarayıcıyı kapat

def megakapat():
    os.system("TASKKILL /IM MEGAsync.exe /F /T")
    time.sleep(20)
    os.system("start C:\\Users\\valid\\AppData\\Local\\MEGAsync\\MEGAsync.exe")



modemreboot()
megakapat()