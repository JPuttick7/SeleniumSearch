import json
import random
import time
from PW import password, email
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def wait_for(sec=2):
    time.sleep(sec)

randomlists_url = "https://www.randomlists.com/data/words.json"
response = requests = requests.get(randomlists_url)
words_list = random.sample(json.loads(response.text)['data'],40)
print('{0} words selected from {1}'.format(len(words_list),randomlists_url))

profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_profile=profile, executable_path=r'C:\Users\jamie\Documents\Python\Search\geckodriver.exe')
wait_for(5)

driver.get("https://login.live.com")
wait_for(5)

try:
    elem = driver.find_element_by_name('loginfmt')
    elem.clear()
    elem.send_keys(email)
    elem.send_keys(Keys.RETURN)
    wait_for(5)
    elem1 = driver.find_element_by_name('passwd')
    elem1.clear()
    elem1.send_keys(password)
    elem1.send_keys(Keys.RETURN)
    wait_for(7)
    

except Exception as e:
    print(e)
    wait_for(4)

url_base = 'https://www.bing.com/search?q='
wait_for(5)
for num, word in enumerate(words_list):
    print('{0}. URL : {1}'.format(str(num + 1), url_base + word))
    try:
        driver.get(url_base + word)
        wait_for()
        print('\t' + driver.find_element_by_tag_name('h2').text)
    except Exception as e1:
            print(e1)
            wait_for()

driver.close()






















