from selenium import webdriver
# import cv2 as cv
import urllib.request
import time

# starting time
start = time.time()
print(time.time()-start)

option = webdriver.ChromeOptions()
option.add_argument('headless')
print(time.time()-start)
browser = webdriver.Chrome( executable_path= r'/mnt/d/SD(SE)/university-project/Nameplate project/chromedriver2',options = option)
print(time.time()-start)
browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
print(time.time()-start)
plateNumber = ""
captchaAnswer = ""

# captcha selector tag : //*[@id="form_rcdl:j_idt32:j_idt37"]

browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys(captchaAnswer)
print(time.time()-start)

# browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').
img = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').get_attribute('src')
print(img)
print(time.time()-start)
urllib.request.urlretrieve(img, "captcha.png")
print(time.time()-start)
print("Printing Title of the Wepage visited")
print(browser.title)
