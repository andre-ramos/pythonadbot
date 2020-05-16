import os
import random
import sys

from Tools.Scripts.treesync import raw_input
from selenium import webdriver
from time import sleep
from random import uniform
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


#url = raw_input("Enter URL to get visits (With http://): ")
url = "http://www.zatnawqy.net/Awnqz"
#proxy_path = raw_input("Enter path to proxy file:")

with open("proxy.txt", "r") as f:
    content = f.readlines()
    f.close()

proxies = num_lines = sum(1 for line in open('proxy.txt'))
print('Loaded %d proxies' %proxies)



# For debugging purposes
#print content[run_through]
run_through = 1
while True:
    #print "Start of loop"
    print("Ran %s times" %run_through)
    try:
        use_proxy = content[run_through]
    except IndexError:
        print("Out of proxies")
        break
    print("Using: %s" %use_proxy)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('chrome://settings/advanced')
    browser.find_element_by_id('privacyContentSettingsButton').click()
    browser.find_element_by_name('popups').click()
    print("Browser started")
    try:
       browser.get(url)
       #print "Opened URL"
       sleep(10)
       browser.find_element_by_id('skiplink').click()
       sleep(10)
       browser.quit()
       #print "Adding one to proxy count"

    except Exception as e:
        print("Skipping proxy. Error occurred")
        # For debugging, uncomment line below
        #print str(e)
        browser.quit()
        run_through += 1
        continue

    run_through += 1

    if run_through >= proxies:
        print("No more proxies")
        break

print('Done!')










