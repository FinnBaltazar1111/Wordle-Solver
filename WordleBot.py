import datetime
import requests
date = datetime.date.today()
url = f"https://www.nytimes.com/svc/wordle/v2/{date:%Y-%m-%d}.json"
response = requests.get(url).json()
print(f"Answer: {response['solution']}")