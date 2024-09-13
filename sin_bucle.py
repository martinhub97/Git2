import pandas as pd
import requests

def execute():
    api_key = "K"
    request_url = f"https://api.nytimes.com/svc/topstories/v2/sports.json?api-key={api_key}"
    
    try:
        response = requests.get(request_url)
        response.raise_for_status() 
        datas = response.json()
        return datas.get('results', [])  
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None

def build_table(json_data):
    try:
        df = pd.json_normalize(json_data)
        df_selected = df[['title', 'abstract', 'url', 'updated_date', 'created_date', 'published_date']]
        return df_selected
    except Exception as e:
        print(f"Error al construir la tabla: {e}")
        return None

data = execute()
if data:
    df_top = build_table(data)
    print(df_top)
