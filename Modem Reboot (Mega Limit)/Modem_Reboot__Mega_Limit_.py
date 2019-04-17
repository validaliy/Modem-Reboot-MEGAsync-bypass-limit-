
from selenium import webdriver
import time
import os
import pyautogui


            #DEĞİŞKENLER
url = "http://192.168.1.1/#__restart.htm"
kullanici_adi = "admin"
sifree = "2EY*12em-"
yenileme = 60

            #DEĞİŞKENLER


def modemreboot():
    driver_path = ".\\Ekler\\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.get(url)
    time.sleep(3)

    kullanici = browser.find_element_by_id("userName")
    sifre = browser.find_element_by_id("pcPassword")
    oturumac = browser.find_element_by_id("loginBtn")

    kullanici.send_keys(kullanici_adi)
    sifre.send_keys(sifree)

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


def dosya_kontrol():
    icon = os.path.isfile('.\\Ekler\\icon.png')
    if icon:
        pro = os.path.isfile('.\\Ekler\\pro.png')
        if pro:
            check()
        else:
            print("pro.png dosyası yok")
    else:
        print("icon.png yok")
        time.sleep(5)

def check():
    try:
        pyautogui.locateCenterOnScreen(".\\Ekler\\icon.png")
        pyautogui.locateCenterOnScreen(".\\Ekler\\pro.png")
        modemreboot()
        print("modem yeniden başlatıldı")
        megakapat()
        print("mega kapatılıp açıldı")
    except TypeError:
        print("Limit Aşımına Rastlanmadı. İptal etmek için ctrl+c basın")
        time.sleep(yenileme)
        check()



modemreboot()