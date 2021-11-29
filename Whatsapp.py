from selenium import webdriver
import time

options = webdriver.ChromeOptions()

try:
    options.add_argument('--user-data-dir=C:\\Users\\Anisn\\AppData\\Local\\Google\\Chrome\\User Data')
    # options.set_headless(True)    
    options.add_argument('--profile-directory=Default')
    # options.headless = True
except Exception as e:
    print(e)

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
# driver.implicitly_wait(15)
driver.get("https://web.whatsapp.com/")
time.sleep(5)
def sendMessage(name, message):

    # user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span[@title = "{}"]'.format(name))
    
    user.click()
    time.sleep(3)
    message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    # message_box = driver.find_element_by_class_name('_13mgZ')
    # message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    print("2")

    message_box.send_keys(message)
    message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
    print("3")
    message_box.click()



sendMessage("SANAN","Hello Buddy")