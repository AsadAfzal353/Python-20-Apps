import requests
import selectorlib
import smtplib, ssl
import time


URL = "http://programmer100.pythonanywhere.com/tours/"

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
    with open("app10-webscrapping/data.txt", "a") as file:
        file.write(extracted + "\n")


def read(extracted):
    with open("app10-webscrapping/data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    while True:
        time.sleep(2)
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read(extracted)

        if extracted != "No upcoming tours" and extracted not in content:
            store(extracted)
            send_email(message="Hey, new event was found!")
    
    