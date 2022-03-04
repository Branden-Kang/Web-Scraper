# Import packages
from bs4 import BeautifulSoup
import requests
import smtplib


def check_price() -> int:
    # get HTML page
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    headers = {"user-agent": user_agent}
    req = requests.get(URL, headers=headers)

    # get price
    soup = BeautifulSoup(req.text, "html.parser")
    span = soup.find("span", {"id": "priceblock_ourprice"}) # <span id="priceblock_ourprice">...</span>
    price = span.text   # XY,ZW €

    return int(price[:2])


def send_email(price):
    # setup smtp and start connection
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("your_email_address", "app_password")

    # create mail
    subject = "Price notification: Mouse Logitech MX 2s"
    body = "The price has fallen to EUR " + str(price) + ".\n Check the link: " + URL
    msg = f"Subject: {subject}\n\n{body}"

    # send mail and quit
    server.sendmail("from", "to", msg)
    server.quit()
    print("Email sent.")


URL = "https://www.amazon.it/gp/product/B072BG9Z8W/"
MY_PRICE = 50

actual_price = check_price()
if actual_price <= MY_PRICE:
    send_email(actual_price)
