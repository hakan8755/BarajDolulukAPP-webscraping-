import requests
import pandas as pd


url = "https://data.ibb.gov.tr/tr/api/3/action/datastore_search"
resource_id = "762b802e-c5f9-4175-a5c1-78b892d9764b"  


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
df.to_excel("barajadüşenyağmur.xlsx", index=False)
print("Veri başarıyla 'barajadüşenyağmur.xlsx' dosyasına kaydedildi.")
    
