
from time import sleep
# import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
 
CHROMEDRIVER = "./ + chromedriver"
 
# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
browser = webdriver.Chrome(service=chrome_service)
 
# Googleアクセス
url = 'https://www.instagram.com'
# url = 'https://www.google.com/'
browser.get(url)

sleep(10)

if url == 'https://www.instagram.com':
    my_id = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    #入力欄を空にする
    my_id.clear()
    password.clear()
    # 入力して、「Enter」を押す
    my_id.send_keys("ここにメールアドレス")
    password.send_keys("ここにパスワード"+ Keys.RETURN)

else:
    # 検索ボックスを特定
    elem = browser.find_element(By.NAME, 'q')
    # 「Selenium」と入力して、「Enter」を押す
    elem.send_keys('Selenium' + Keys.RETURN)

sleep(20)
