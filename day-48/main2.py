from selenium import webdriver
from selenium.webdriver.common.by import By
from amazoncaptcha import AmazonCaptcha

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com.br/Lavadora-Alta-Press%C3%A3o-1750PSI-110V-WAP-OUSADAPLUS/dp/B077PT41YL"
           "/ref=sr_1_5?crid=2R9425XD5HR6I&dib=eyJ2IjoiMSJ9.OFw7B9jIg439oL7bSJOASv6yknuwosCZCJAGOtb1ylEQbIBuO4Zd76zyEJ"
           "eIZnSk-0LSm9qByE29qMzMoELo2Hg5c_R6nc-HpNqDw6YTqxP9VtP4jJYgI8q5EPlcW2FUm0Gzbe3H0rq1pUYSHzUebDh1O0ade94_"
           "rrlv5WtARcIeeyK7ElQw_3XQbitFCA2_VeJs9ySevYrPNANv8vzDk7DF6uuLt8Tqd7bpkRFoq_WkLbQ5czqdy3_xk1IttQpbyRZi3Jl6"
           "v1S1mR2eoQCqJiXV4NqfVfZjip_Ttwlat9o.tNSU3rX5PhyvMRzImJQyJo5I4OO5N_U9WojTg1LFkbc&dib_tag=se&keywords=wap%2B"
           "lavadora%2Bde%2Balta%2Bpress%C3%A3o&qid=1713176307&sprefix=wap%2Caps%2C216&sr=8-5&ufe=app_do%3Aamzn1.fos.4"
           "bddec23-2dcf-4403-8597-e1a02442043d&th=1")

link = driver.find_element(By.XPATH, "//div[@class = 'a-row a-text-center']//img").get_attribute('src')
captcha = AmazonCaptcha.fromlink(link)
captcha_value = AmazonCaptcha.solve(captcha)
driver.find_element(By.ID, "captchacharacters").send_keys(captcha_value)
button = driver.find_element(By.CLASS_NAME, "a-button-text")
button.click()

price_brl = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_brl_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is {price_brl.text},{price_brl_cents.text}")

driver.quit() # entire browser

