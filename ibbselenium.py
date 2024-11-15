import requests
import pandas as pd

url = "https://data.ibb.gov.tr/api/3/action/datastore_search"
resource_id = "af0b3902-cfd9-4096-85f7-e2c3017e4f21" 

limit = 1000  
offset = 0  
all_records = []  
while True:
   
    params = {
        "resource_id": resource_id,
        "limit": limit,
        "offset": offset
    }
    response = requests.get(url, params=params)
    data = response.json()


    if data["success"]:
        records = data["result"]["records"]
        if not records:  
            break
        all_records.extend(records)  

        offset += limit
    else:
        print("Veri çekme işlemi başarısız.")
        break
    
df = pd.DataFrame(all_records)
df.to_excel("6000_ve_sonrasi_tum_yagis_verisi.xlsx", index=False)
print("Veri başarıyla '6000_ve_sonrasi_tum_yagis_verisi.xlsx' dosyasına kaydedildi.")