from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

service = Service("C:/webdrivers/chromedriver.exe")


options = Options()
options.headless = False  



def get_data_for_year_month(driver, year, month):
    try:
        
        dynamic_url = f"https://www.wunderground.com/history/monthly/tr/istanbul/LTBA/date/{year}-{month:02d}"
        driver.get(dynamic_url)

      
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="inner-content"]/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[5]/tr/td[2]'))
        )

       
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="inner-content"]/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[5]/tr/td[2]'))
        )


        xpath = '//*[@id="inner-content"]/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[5]/tr/td[2]'

       
        element = driver.find_element(By.XPATH, xpath)
        value = element.text

      
        if value == "0.00":
            print(f"Veri 0.00 olarak çekildi: {year}-{month:02d}")
        else:
            print(f"Veri başarıyla çekildi: {value} - {year}-{month:02d}")

        return value

    except Exception as e:
        print(f"{year}-{month:02d} için veri çekilirken hata: {e}")
        return None



def start_driver():
    driver = webdriver.Chrome(service=service, options=options)
    return driver



def fetch_data():
    data = []
    driver = start_driver()

    for year in range(2014, 2025):  
        for month in range(1, 13):  
            if year == 2024 and month > 11: 
                break
            print(f"Veri çekiliyor: {year}-{month:02d}")
            value = get_data_for_year_month(driver, year, month)
            if value:
                data.append([year, month, value])

   
    df = pd.DataFrame(data, columns=["Yıl", "Ay", "Deniz Basıncı"])
    df.to_excel("deniz_basinci_veri.xlsx", index=False)

    driver.quit()



fetch_data()
