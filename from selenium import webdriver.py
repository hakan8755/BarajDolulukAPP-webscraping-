from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
veriler = []
driver = webdriver.Chrome()
ay=8
yil=2009



while yil<2024:
    link=f"https://www.timeanddate.com/weather/turkey/istanbul/historic?month={ay}&year={yil}"
    driver.get(link)
    time.sleep(3)
    
    try:
       
        tablo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'zebra tb-wt fw tb-hover')]"))
        )
        
       
        try:
            dusuk_sicaklik = tablo.find_element(By.XPATH, ".//tr[2]/td[1]").text
        except NoSuchElementException:
            dusuk_sicaklik = "Veri yok"
        
        try:
            dusuk_nem = tablo.find_element(By.XPATH, ".//tr[2]/td[2]").text
        except NoSuchElementException:
            dusuk_nem = "Veri yok"
        
        try:
            dusuk_basinc = tablo.find_element(By.XPATH, ".//tr[2]/td[3]").text
        except NoSuchElementException:
            dusuk_basinc = "Veri yok"

        try:
            ortalama_sicaklik = tablo.find_element(By.XPATH, ".//tr[3]/td[1]").text
        except NoSuchElementException:
              ortalama_sicaklik = "Veri yok"
        
        try:
              ortalama_nem = tablo.find_element(By.XPATH, ".//tr[3]/td[2]").text
        except NoSuchElementException:
              ortalama_nem = "Veri yok"
        
        try:
              ortalama_basinc = tablo.find_element(By.XPATH, ".//tr[3]/td[3]").text
        except NoSuchElementException:
              ortalama_basinc = "Veri yok"

        try:
            yuksek_sicaklik = tablo.find_element(By.XPATH, ".//tr[1]/td[1]").text
        except NoSuchElementException:
             yuksek_sicaklik = "Veri yok"
        
        try:
             yuksek_nem = tablo.find_element(By.XPATH, ".//tr[1]/td[2]").text
        except NoSuchElementException:
             yuksek_nem = "Veri yok"
        
        try:
             yuksek_basinc = tablo.find_element(By.XPATH, ".//tr[1]/td[3]").text
        except NoSuchElementException:
             yuksek_basinc = "Veri yok"

       
        veriler.append([yil, ay, yuksek_sicaklik, yuksek_nem, yuksek_basinc,
                        dusuk_sicaklik, dusuk_nem, dusuk_basinc,
                        ortalama_sicaklik, ortalama_nem, ortalama_basinc])

    except TimeoutException:
        print(f"{yil}-{ay} için tablo bulunamadı veya yüklenemedi.")
   
    ay += 1

    if ay == 13:
        yil += 1
        ay = 1


driver.quit()

df = pd.DataFrame(veriler, columns=["Yıl", "Ay", "Yüksek Sıcaklık", "Yüksek Nem", "Yüksek Basınç",
                                    "Düşük Sıcaklık", "Düşük Nem", "Düşük Basınç",
                                    "Ortalama Sıcaklık", "Ortalama Nem", "Ortalama Basınç"])

df.to_excel("istanbul_weather_summary.xlsx", index=False)
print("Veriler Excel dosyasına yazıldı.")