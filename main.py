from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://monkeytype.com/')

time.sleep(2)
reject = driver.find_element(By.CLASS_NAME, value='rejectAll')
reject.click()

time.sleep(1)
desired_duration = 30
start_time = time.time()
while (time.time() - start_time) < desired_duration:
    words = driver.find_element(By.CSS_SELECTOR, '#words .active')
    keys = driver.find_element(By.ID, value='wordsInput')
    keys.send_keys(f'{words.text} ')

time.sleep(1)
wpm = driver.find_element(By.CLASS_NAME, value='bottom')
print(f'Words per minute: {wpm.text}')
driver.quit()









# for _ in range(20):
# words = driver.find_elements(By.CLASS_NAME, value='word')
# words = driver.find_element(By.CSS_SELECTOR, '#words .active')
# print(words.text)
# keys = driver.find_element(By.ID, value='wordsInput')
# keys.send_keys(f'{words.text} ')
# words = driver.find_elements(By., 'words')
# print(words.text)
#
# for word in words:
#     print(word.text)
#     keys = driver.find_element(By.ID, value='wordsInput')
#     keys.send_keys(f'{word.text} ')
# //*[@id="words"]/div[2]
