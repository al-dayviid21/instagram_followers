import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

URL = "https://www.amazon.com/dp/B08PWR7464/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
MY_EMAIL = "onyitombara@gmail.com"
PASSWORD = "08135303868"
response = requests.get(url=URL,
                        headers=headers)
amazon_webpage = response.text
soup = BeautifulSoup(amazon_webpage, "lxml")
price_with_dollar_sign = soup.find(name="span", class_ ="a-offscreen").getText()
price_as_lst = price_with_dollar_sign.split("$")
price_without_dollar_sign = float(price_as_lst[1])

product_title = soup.find(name="span", id="productTitle").getText()

if price_without_dollar_sign < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= "davidalabintei97@gmail.com",
            msg=f"Subject: Amazon Price Alert!\n\n{product_title} now at {price_with_dollar_sign}\n{URL}"
        )

