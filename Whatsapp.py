from selenium import webdriver
import time

options = webdriver.ChromeOptions()

try:
    options.headless = True
except Exception as e:
    print(e)

driver = webdriver.Chrome(executable_path='../back-end/bots/chromedriver',options=options)

def sendMessage(name, message):
    try:
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
        message_box = driver.find_element_by_xpath('//html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
        message_box.send_keys(message)
        message_box = driver.find_element_by_xpath('//button[@class="_4sWnG]')
        message_box.click()
        time.sleep(2)
    except Exception as e:
        print(e)
