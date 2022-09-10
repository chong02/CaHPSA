import pandas as pd
import requests

url = 'https://data.chhs.ca.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22641c5557-7d65-4379-8fea-6b7dedbda40b%22'
request = requests.get(url)
json_object = request.json()

data_file = pd.DataFrame(json_object['result']['records'])
data_file.to_csv('ca_healthcare_facilities.csv', index=False)