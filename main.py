import time
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from curl_cffi import requests


def get_cookies():
    with uc.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
        driver.implicitly_wait(60)
        driver.get("https://www.ozon.ru")
        driver.find_element(By.CSS_SELECTOR, "#stickyHeader")
        user_agent = driver.execute_script("return navigator.userAgent")
        cookies = driver.get_cookies()

    cookies_dict = {i["name"]:i["value"] for i in cookies}

    return user_agent, cookies_dict


user_agent, cookies_dict = get_cookies()

response = requests.get("https://www.ozon.ru/search/?text=ps+vita&from_global=true", cookies=cookies_dict, headers={
    "user-agent": user_agent
})

with open("html.html", "w", encoding="utf-8") as file:
    file.write(response.text)
