from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")


email = browser.find_element_by_class_name("whsOnd")
email.send_keys('iamnamananand996@gmail.com')
email.send_keys(Keys.RETURN)

time.sleep(4)

pwd = browser.find_element_by_class_name("whsOnd")
pwd.send_keys('naman@anand')
pwd.send_keys(Keys.RETURN)

time.sleep(40)

for i in range(10):

    time.sleep(3)
    compose = browser.find_element_by_class_name("z0")
    browser.implicitly_wait(5)
    compose.click()

    time.sleep(3)
    to_email = browser.find_element_by_class_name("vO")
    to_email.send_keys("iamnamananand2@gmail.com")
    to_email.send_keys(Keys.RETURN)

    time.sleep(2)

    msg = browser.find_element_by_class_name("Am")
    msg.send_keys("test")
    msg.send_keys(Keys.RETURN)

    time.sleep(2)
    send = browser.find_element_by_class_name("gU")
    browser.implicitly_wait(5)
    send.click()

    time.sleep(5)







