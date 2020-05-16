import os
import random
import sys

from Tools.Scripts.treesync import raw_input
from selenium import webdriver
from time import sleep

#url = raw_input("Enter URL to get visits (With http://): ")
url = "http://adf.ly/1Yw4oO"
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
    print("Browser started")
    try:
       browser.get(url)
       #print "Opened URL"
       sleep(10)
       #browser.find_element_by_id('skip_ad_button').click()
       browser.find_element_by_id('skip_ad_button').click()
       sleep(10)
       browser.quit()
       #print "Adding one to proxy count"

    except Exception as e:
        print("Skipping proxy. Error occured")
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










