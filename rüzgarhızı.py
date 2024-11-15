import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


start_year = 2010
end_year = 2020
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

data = []

for year in range(start_year, end_year + 1):
    for month in months:
        url = f"https://weatherandclimate.com/istanbul/{month}-{year}"
        driver.get(url)
        time.sleep(5)

        try:
            wind_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//html/body/main/div[1]/div/div[3]/div/div/table/tbody/tr[11]/td[3]"))
            )
            wind_speed = wind_element.text.strip()
            data.append([f"{month.capitalize()} {year}", wind_speed])
            print(f"{month.capitalize()} {year}: {wind_speed}")
        except Exception as e:
            print(f"{month.capitalize()} {year}: Veri bulunamadı - Hata: {str(e)}")
            data.append([f"{month.capitalize()} {year}", "N/A"])

driver.quit()

df = pd.DataFrame(data, columns=["Tarih", "Average Wind"])
df.to_excel("average_wind_data.xlsx", index=False)
print("Veriler Excel dosyasına başarıyla kaydedildi.")
