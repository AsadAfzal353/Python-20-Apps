import requests # useful to browse api
from send_email import send_email

api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?"\
      "q=tesla&"\
      "sortBy=publishedAt&"\
      "apiKey=890603a55bfa47048e4490069ebee18c&" \
      "language=en"

# api_key = "8ebbdb85abe843e7a5d6af5767c5b673"
# url = "https://api.worldnewsapi.com/search-news?language=es&text=covid-19+corona+SARS-CoV-2+coronavirus"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    body = body + article["title"] + article["description"] + 2*"\n"
    print(article["title"])

body = body.encode("utf-8")
send_email(message=body)