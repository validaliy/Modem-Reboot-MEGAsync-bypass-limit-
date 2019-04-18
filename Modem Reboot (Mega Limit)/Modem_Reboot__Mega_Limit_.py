
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



def	giris(): #kullanıcı adı ve şifre girerek giriş yap
    driver_path = ".\\Ekler\\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.get(url)
    time.sleep(5)

    kullanici = browser.find_element_by_id("userName")
    sifre = browser.find_element_by_id("pcPassword")
    oturumac = browser.find_element_by_id("loginBtn")

    kullanici.send_keys(kullanici_adi)
    sifre.send_keys(sifree)

    oturumac.click()
    time.sleep(5)

def giris2(): #cookie ile giriş yap javascript kullanarak
    driver_path = ".\\Ekler\\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.get(url)
    time.sleep(5)
    browser.execute_script('document.cookie = "Authorization=Basic YWRtaW46MkVZKjEyZW0t"')
    time.sleep(1)
    browser.execute_script('window.location.reload()')
    time.sleep(5)
	
	
def modemreboot():
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


def main():
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
        giris()
        modemreboot()
        print("modem yeniden başlatıldı")
        megakapat()
        print("mega kapatılıp açıldı")
    except TypeError:
        print("Limit Aşımına Rastlanmadı. İptal etmek için ctrl+c basın")
        time.sleep(yenileme)
        check()


main()