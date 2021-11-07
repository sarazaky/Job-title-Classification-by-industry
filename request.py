import requests
import sys

job = sys.argv[1]

url = f'http://localhost:5000/predict_api/{job}'
r = requests.get(url)

print(r.json())