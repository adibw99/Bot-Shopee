import time
from selenium import webdriver
import pyfiglet as f
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import schedule

options = Options()
options.headless = True
options.add_argument("--incognito")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
prefs = {'profile.default_content_setting_values': {'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
options.add_experimental_option("prefs", prefs)

# LOKASI DRIVER WEBCHROEM DI KOMPUTER

browser = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')

actionChains = ActionChains(browser)





#INFO AUTOR

def authors():
    style = f.figlet_format("Bot Shopee V 1 . 1")
    print(style)
    print("\033[31m----- \033[93mVersi  : \033[92mBot Shopee Versi 1.1 \033[31m      -----")
    print("\033[31m----- \033[93mAuthor : \033[92mAdib B  \033[31m                   -----")
    print("\033[31m----- \033[93mNote   : \033[92mGak Usah Di Share Tolol!   \033[31m-----")

def finish():
    style = f.figlet_format("HOREE DAPET :P")
    time.sleep(2)
    print(style)

def error():
    style = f.figlet_format("SYSTEM ERROR SHOPE TELAH DI PERBARUI")
    time.sleep(2)
    print(style)
#GET COOKIE LOGIN SHOPEE

def load_cookies():
    browser.get("https://shopee.co.id")
    browser.add_cookie({'name': 'SPC_EC', 'value': cookie})
    browser.get_cookies()
    time.sleep(2)
    print('\033[32m[+] Login Akun Berhasil')

#FUNGSI TOMBOL BELI

def tombol_beli():
    try:

        varians = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Biru')]")))
        browser.execute_script("arguments[0].click();", varians)

        # ukuran = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'40')]")))
        # browser.execute_script("arguments[0].click();", ukuran)

        # TOMBOL BELI
        
        beli = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'beli sekarang')]")))
        # WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[3]/div/div[5]/div/div/button[2]')))
        browser.execute_script("arguments[0].click();", beli)
        print("\033[32m[+] INFO: Barang Masuk Dalam Keranjang! Saat\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

        #TOMBOL CHECKOUT
        checkout = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[4]')))
        browser.execute_script("arguments[0].click();", checkout)
        print("\033[32m[+] INFO: Barang otw Checkout!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

        #TOMBOL PENGIRIMAN SETIAP SAAT REGULER
        klik_modal = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[5]')))
        # /html/body/div[1]/div/div[3]/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[5]
        # /html/body/div[1]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[5]
        browser.execute_script("arguments[0].click();", klik_modal)
        print("\033[32m[+] INFO: pilih Pengiriman!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
        
        jenis_pengiriman = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]')))
        browser.execute_script("arguments[0].click();", jenis_pengiriman)
        print("\033[32m[+] INFO: Jenis Pengiriman Telah Di-Set!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
        
        #CARGO
        # /html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]
        
        #STANDAR
        # /html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]

        ok_buttonPengiriman = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div/button[2]')))
        browser.execute_script("arguments[0].click();", ok_buttonPengiriman)
        print("\033[32m[+] INFO: Pengiriman Telah Di-Set!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

        
        #TOMBOL PESAN

        pesanan = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[4]/div[2]/div[7]/button')))
        # WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[4]/div[2]/div[7]/button')))
        browser.execute_script("arguments[0].click();", pesanan)
        print("\033[32m[+] INFO: Pesanan Dibuat!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

        #TOMBOL BAYAR
        bayar = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.ID, 'pay-button')))
        bayar.click()
        print("\033[32m[+] INFO: Proses Bayar!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
        
        # INISIALISASI PIN NUMBER SHOPE PASTIKAN DI CONFIG PIN BENAR
        pin_shopee = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[3]/div[1]')))
        actionChains.send_keys_to_element(pin_shopee).send_keys(pin_number).perform()
        

        # KONFIRMASI PEMBAYARAN
        konfirmasi = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[4]/div[2]')))
        konfirmasi.click()
        print("\033[32m[+] INFO: Barang Telah Dipesan!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

        finish()
       
    except NoSuchElementException as e:
        print(e)
        error()
# NWhBTURNaDBleHZlV1JJUuE0SvJYywlVzJjNOKtW9aXvgztEmJMIQE620su5+9qN1CRJRhQzr0B4KtmmbqbDsbfaM21OCZgfgDc/6AnKvmzSVV2u4tcTC9xpF8EBFLgGr705G8TZT1oCEdFQpdO5ecSAUS+r+Occ4rG7/Gzz8Es=
authors()
print ("\033[32m[+] Anda Harus login")
cookie=input("User Login: ")
pin_number=000000
print("")
# MENU UTAMA PROGRAM DI EKSEKUSI
def main():
    jam_device = time.strftime("%H:%M:%S", time.localtime())
    time.sleep(3)
    load_cookies()
    link_produk = input("Masukkan Link produk: ")
    # 'https://shopee.co.id/Emas-UBS-1-Gram-Logam-Mulia-Garansi-Uang-Kembali-Include-Sertifikat-i.13385605.440072920'
    browser.get(link_produk)
    
    f.print_figlet("Main Menu")
    print ("\033[32m[+] Menu Pilihan Check Out")
    print (" \033[31m   1. Metode Waktu OnTime")
    print (" \033[31m   2. Metode Refresh Browser")
    Pilihan_Menu = input("\033[32m[+]Pilihan Anda adalah : \033[31m")
    if Pilihan_Menu == "1":
        jam = int(input("\033[32m[+] Masukan Jam untuk memulai beli : "))
        menit = int(input("\033[32m[+] Masukan Menit untuk memulai beli : "))
        detik = int(input("\033[32m[+] Masukan Detik untuk memulai beli : "))
        waktu = '{:02d}:{:02d}:{:02d}'.format(jam, menit, detik)
        def print_info():    
            print("\033[32m[+] INFO:\033[31m", waktu , "\033[93mWAKTU TUNGGU.!")
        print_info()
        
        while jam_device != waktu :
            jam_device_INT = int(time.strftime("%H%M%S", time.localtime()))
            waktu_int='{:02d}{:02d}{:02d}'.format(jam, menit, detik)
            nilai = int(waktu_int)
    
            
            if jam_device_INT < nilai:
                import sys

            else:
                print("\033[32m[+] INFO:\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mWAKTU PEMBELIAN.!" )
                browser.refresh()
                
                break
        tombol_beli()
        

    if Pilihan_Menu == "2":
        jam = int(input("\033[32m[+] Masukan Jam untuk memulai beli : "))
        menit = int(input("\033[32m[+] Masukan Menit untuk memulai beli : "))
        detik = int(input("\033[32m[+] Masukan Detik untuk memulai beli : "))
        waktu = '{:02d}:{:02d}:{:02d}'.format(jam, menit, detik)
        while jam_device != waktu :
            jam_device_INT = int(time.strftime("%H%M%S", time.localtime()))
            waktu_int='{:02d}{:02d}{:02d}'.format(jam, menit, detik)
            nilai = int(waktu_int)

            if jam_device_INT < nilai:
                print("\033[32m[+] INFO:\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mWAKTU BELUM MULAI.!" )
                browser.refresh()
            else:
                break
        tombol_beli()


if __name__ == "__main__":
    main()