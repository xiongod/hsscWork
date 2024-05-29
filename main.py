import sys
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

index = 32
#while index < 443:
while index < 42:
    print(index)
    try:
        time.sleep(60)
        # 打开网页
        url = 'https://mitingshu.com/play/7406-0-'+str(index)+'.html'  # 替换为你要打开的网页URL
        driver.get(url)
        wait = WebDriverWait(driver, 3)

        title_class = 'f-22'
        title_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'f-22')))
        title = title_element.text
        #print(title)

        iframe = driver.find_element(By.ID, 'cciframe')
        driver.switch_to.frame(iframe)
        element_in_iframe = driver.find_element(By.ID, 'jp_audio_0')
        src = element_in_iframe.get_attribute('src')
        #print(src)

        with open('./data.txt', 'a', encoding='utf-8') as file:
            file.write(title+'#'+src+'\n')
        index += 1
    except Exception as e:
        print(e)


# 关闭浏览器窗口
driver.quit()
