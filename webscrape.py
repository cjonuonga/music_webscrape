import requests
import selectorlib
import smtplib, ssl
import os
import time

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    ''' Scrape the page sourcce from the URL'''
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "onuongacaleb@gmail.com"
    password = "oxtn muet axyn aymj"

    receiver = "onuongacaleb@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email was sent!")


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")

def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    # while True: use pythonanywhere server instead in the future!
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in "data.txt":
            store(extracted)
            send_email(message="Hey, new event was found!")
    # time.sleep(2) use pythonanywhere server instead in the future!

