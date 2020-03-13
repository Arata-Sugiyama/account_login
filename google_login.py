from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# アカウントログイン
wait_time=30


driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("ログインURL")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 



# ユーザーIDの入力
user_id_box = driver.find_element_by_id("identifierId")
user_id_box.send_keys("ユーザーID")

driver.find_element_by_id('identifierNext').click()

# パスワード入力
"""
下記では上手く動作しませんでした
user_pass_box = driver.find_element_by_id("password")
user_id_box.send_keys("arata2412")
driver.find_element_by_id('passwordNext').click()
"""

login_pw="arata2412"

login_pw_xpath = '//*[@パスワード"]'
WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
driver.find_element_by_name("password").send_keys(login_pw)
time.sleep(1)

driver.find_element_by_xpath(login_pw_xpath).click()

