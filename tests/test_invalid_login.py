from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")


    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    username.send_keys("kullanıcıadı")
    password.send_keys("şifre")
    login_button.click()

    time.sleep(1)

    error_message = driver.find_element(By.ID, "flash").text

    if "Your username is invalid!" in error_message:
        print("Testi geçti: Hata mesajı görünüyor.")
    else:
        print("Test başarısız: Hata mesajı beklenildiği gibi değil.")

finally:
    driver.quit()
