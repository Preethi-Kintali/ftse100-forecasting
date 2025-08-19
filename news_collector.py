import requests
import pandas as pd

API_KEY = "e15bf0811648417f941aa8d82a9d24e8"
url = f"https://newsapi.org/v2/everything?q=FTSE+100&language=en&sortBy=publishedAt&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

articles = data.get("articles", [])

df = pd.DataFrame([{
    "source": a["source"]["name"],
    "title": a["title"],
    "description": a["description"],
    "url": a["url"],
    "publishedAt": a["publishedAt"]
} for a in articles])

df.to_csv("ftse100_news.csv", index=False)
print("✅ News data saved to ftse100_news.csv")
