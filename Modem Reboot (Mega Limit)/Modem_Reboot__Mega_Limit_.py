
from selenium import webdriver
import time
from os import system
import re
import win32gui

            #DEĞİŞKENLER
url = "http://192.168.1.1/#__restart.htm"
kullanici_adi = "admin"
sifree = "şifre"
yenileme = 300
temizle = os.system("cls")

            #DEĞİŞKENLER



def	giris(): #kullanıcı adı ve şifre girerek giriş yap

    kullanici = browser.find_element_by_id("userName")
    sifre = browser.find_element_by_id("pcPassword")
    oturumac = browser.find_element_by_id("loginBtn")

    kullanici.send_keys(kullanici_adi)
    sifre.send_keys(sifree)

    oturumac.click()
    time.sleep(5)


def giris_cookie(): #cookie ile giriş yap javascript kullanarak
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
    print("modem yeniden başlatılıyor")
    time.sleep(20)
    browser.quit() #tarayıcıyı kapat
    print("modem yeniden başlatıldı")
    

def megakapat():
    os.system("TASKKILL /IM MEGAsync.exe /F /T")
    print("mega kapatıldı")
    time.sleep(20)
    os.system("start C:\\Users\\valid\\AppData\\Local\\MEGAsync\\MEGAsync.exe")
    print("mega  açıldı")




def acik_pencereler():
    def callback(handle, data):
        titles.append(win32gui.GetWindowText(handle))

    titles = []
    win32gui.EnumWindows(callback, None)
    return titles



while True:
    basliklar = acik_pencereler()
    basliklar = ''.join(map(str, basliklar)) #aık pencereleri arraydan string'e çevirir
    sonuc = re.search("aktarma kotası", basliklar) #açık uygulamalarda "aktarma kotası" ismi varsa "Ücretsiz aktarma kotası aşıldı"
    if sonuc:
        driver_path = ".\\chromedriver.exe"
        chrome_driver = os.path.isfile(driver_path)
        if chrome_driver:
            browser = webdriver.Chrome(executable_path=driver_path)
            browser.get(url)
            time.sleep(5)
            giris()
            modemreboot()
            megakapat()
        else:
            print("chromedriver.exe yok")
    else:
        print("Kota aşımı Yok")
        time.sleep(yenileme)