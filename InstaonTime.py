from selenium import webdriver
from time import sleep
import time
from datetime import datetime

class InstaMsg:
    def __init__(self, username, pw, name, msg):
     
        self.driver = webdriver.Chrome()
        self.username = username
        self.pw = pw
        self.name = name
        self.msg = msg
        
        self.driver.get("https://www.instagram.com")
        sleep(4)
#for username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
#for password
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
            .send_keys(pw)
#for login
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")\
            .click()
        sleep(4)
#for not saving info
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
            .click()
        sleep(2)
#for not now
        
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
            .send_keys(name)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/div/span")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")\
            .send_keys(msg)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")\
            .click()

        sleep(2)
        self.driver.quit()


Uname = input("Enter your username:")
Pas = input("Enter your Password:")

Name = input("Enter the person's ID:")
Msg = input("Enter the message:")
print("Input Time")
hour = input("Hour:")
Min = input("Minutes:")
T1 = hour+":"+Min

while(True):
    now = datetime.now()
    T2 = now.strftime("%H:%M")
    if T2==T1:
        Bot = InstaMsg(Uname, Pas, Name, Msg)
        break
