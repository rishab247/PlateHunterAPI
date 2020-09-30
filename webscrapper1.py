from selenium import webdriver
# import cv2 as cv
import urllib.request


option = webdriver.ChromeOptions()
option.add_argument('headless')

browser = webdriver.Chrome(options=option)
browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')

plateNumber = ""
captchaAnswer = ""

# captcha selector tag : //*[@id="form_rcdl:j_idt32:j_idt37"]

browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys(captchaAnswer)


# browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').
img = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').get_attribute('src')
print(img)
urllib.request.urlretrieve(img, "captcha.png")

# x = browser.get(img)
# browser.find_element_by_class_name("ui-button-text").click()
print("Printing Title of the Wepage visited")
print(browser.title)
