from selenium import webdriver
import urllib.request
import base64

import os
os.system('ls')
o = webdriver.ChromeOptions()
o.add_argument("--headless")
o.add_argument("--disable-gpu")
o.add_argument("--no-sandbox")
o.add_argument("enable-automation")
o.add_argument("--disable-infobars")
o.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome( executable_path= r'/home/site/wwwroot/chromedriver2',options = o)
try:
    browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
    print(browser.title)
    plateNumber = ""
    captchaAnswer = ""

    browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
    browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
    browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys(captchaAnswer)
    # print(time.time() - start)

    # browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').
    img = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').get_attribute('src')
    print(img)
    # print(time.time() - start)
    urllib.request.urlretrieve(img, "captcha.png")
    z = base64.b64encode(urllib.request.urlopen(img).read())
    print(z)
    browser.close()
except Exception as e :
    print(e)
    browser.close()



