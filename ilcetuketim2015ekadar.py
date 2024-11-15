import requests
import pandas as pd


url = 'https://data.ibb.gov.tr/api/3/action/datastore_search?resource_id=9d67d3b9-d81f-4cb4-a99c-27c0db5e8b40&limit=100'

response = requests.get(url)


if response.status_code == 200:

    data = response.json()
    

    records = data.get('result', {}).get('records', [])
    
   
    if records:
        df = pd.DataFrame(records)
        
        
        df.to_excel('api_su_tuketim.xlsx', index=False)
        print("Veriler başarıyla 'api_su_tuketim.xlsx' dosyasına kaydedildi.")
    else:
        print("API'den veri alınamadı veya veri boş.")
else:
    print(f"API isteği başarısız oldu, hata kodu: {response.status_code}")
