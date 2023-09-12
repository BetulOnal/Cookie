from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options =webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5 #time.time şuanki zamanı saniye cinsinden çeviriyo
five_min = time.time() + 60*2 # 5minutes
cookie= driver.find_element(By.CSS_SELECTOR,"#cookie")

all_ıd = driver.find_elements(By.CSS_SELECTOR, "#store div")
all_ıd_list = [item.get_attribute("id") for item in all_ıd]

while True:
    cookie.click()
    if time.time()>timeout:
        my_money = driver.find_element(By.XPATH, '//*[@id="money"]').text
        if "," in my_money:
            my_money = my_money.replace(",","")

        all_amount = driver.find_elements(By.CSS_SELECTOR, "#store b")[:8]
        all_amount_list = [int(item.text.split("-")[1].replace(",", "")) for item in all_amount]

        for x in all_amount_list:
            if int(my_money) < x:
                index = (all_amount_list.index(x))-1
                name = all_ıd_list[index]
                driver.find_element(By.CSS_SELECTOR, f"#{name}").click()
                timeout = time.time() + 5
                break

        if time.time() > five_min:
            print("game finish")
            break

driver.quit()





