import requests
import os

API_KEY = os.getenv("API_KEY")

#url = f'https://api.the-odds-api.com/v4/sports?apiKey={API_KEY}'

url = f'https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey={API_KEY}&regions=us&markets=h2h,spreads&oddsFormat=american'

response = requests.get(url)

data = response.json()

print(data)