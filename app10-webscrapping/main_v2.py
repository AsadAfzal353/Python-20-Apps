import requests
import selectorlib
import smtplib, ssl
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
connection = sqlite3.connect("app10-webscrapping/data_fetch.db")

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("app10-webscrapping/extract.yaml")
    value = extractor.extract(source)["tours"] # the key has to be reflected in the yaml file
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username= "app8flask@gmail.com"
    password = "here_goes_your_gmail_password"

    receiver = "app8flask@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    
    print("Email was sent")


def store(extracted):
    row = [item.strip() for item in extracted.split(",")]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()


def read(extracted):
    row = [item.strip() for item in extracted.split(",")]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows

if __name__ == "__main__":
    while True:
        time.sleep(2)
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                # send_email(message="Hey, new event was found!") # CureMD firewall issue
    
    