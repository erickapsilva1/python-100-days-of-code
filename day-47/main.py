from bs4 import BeautifulSoup
import requests
import smtplib

my_email = ""
password = ""
TARGET_PRICE = 200.00

product_link = "https://www.amazon.com.br/dp/B0CF3JFY5T/?coliid=I33337ULZSXDOL&colid=3AM8Y7XG1EQS4&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

response = requests.get(url=product_link, headers=headers)
product_page = response.text

soup = BeautifulSoup(response.content, "html.parser")
whole_price = soup.find(name="span", class_="a-price-whole")
fraction_price = soup.find(name="span", class_="a-price-fraction")


current_price = float(f"{whole_price.getText()}{fraction_price.getText()}".replace(",","."))

if current_price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="",
                            msg=f"Subject:Amazon Price Alert\n\n"
                                f"Super Mario Bros. Wonder \n\n {product_link}"
                            )



