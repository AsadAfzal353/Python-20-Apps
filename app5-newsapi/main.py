import requests # useful to browse api
from send_email import send_email

topic = "tesla"
api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&"\
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
for article in content["articles"][:20]:
    body = body + article["title"] + article["description"] + 2*"\n"
    print(article["title"])

body = body.encode("utf-8")
send_email(message=body)

# To download any file from web
"""
url2 = "https://media.licdn.com/dms/image/C4D03AQGo_UjpPJ-Gsg/profile-displayphoto-shrink_800_800/0/1644442954023?e=2147483647&v=beta&t=2dTPjCvQtjHrLeFKmUmTlgJBNufSxJVKJcEGz-neCA0"
response2 = requests.get(url2)
with open("app5-newsapi/image.jpg", "wb") as file:
    file.write(response2.content)
"""