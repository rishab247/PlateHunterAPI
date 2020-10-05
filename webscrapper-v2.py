from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import base64
import os

option = webdriver.ChromeOptions()
# option.add_argument('headless')

browser = webdriver.Chrome(options=option)
browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')

print('Opening URL...')

plateNumber = "MH01AE8017"
captchaAnswer = ""

print('Plate Number:', plateNumber)

browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
print('Entering first part:',plateNumber[:-4])
browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
print('Entering second part:',plateNumber[-4:])

captcha = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]')

img_captcha_base64 = browser.execute_async_script("""
    var ele = arguments[0], callback = arguments[1];
    ele.addEventListener('load', function fn(){
      ele.removeEventListener('load', fn, false);
      var cnv = document.createElement('canvas');
      cnv.width = this.width; cnv.height = this.height;
      cnv.getContext('2d').drawImage(this, 0, 0);
      callback(cnv.toDataURL('image/jpeg').substring(22));
    }, false);
    ele.dispatchEvent(new Event('load'));
    """, captcha)

with open(r"captcha.jpg", 'wb') as f:
    f.write(base64.b64decode(img_captcha_base64))
captchaAnswer = input()
browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys(captchaAnswer)
browser.find_element_by_class_name("ui-button-text").click()

time.sleep(1)

try:
    browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt14"]/div')
    print('Invalid Captcha!')
    os._exit(0)
except:
    pass

registrationNumber = ""
registrationDate = ""
chassisNumber = ""
engineNumber = ""
ownerName = ""
vehicleClass = ""
fuelType = ""
makerOrModel = ""
fitnessUpto = ""
insuranceUpto = ""
fuelNorms = ""
roadTaxPaidUpto = ""
nocDetails = ""

try:
    x = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[1]/td[2]')))
except TimeoutException:
    print('Invalid Car Number Plate!')
    os._exit(0)
except:
    print('An Error Occurred!')
    os._exit(0)

try:
    registrationNumber = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[1]/td[2]').text
except:
    pass

try:
    registrationDate = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[1]/td[4]').text
except:
    pass

try:
    chassisNumber = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[2]/td[2]').text
except:
    pass

try:
    engineNumber = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[2]/td[4]').text
except:
    pass

try:
    ownerName = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[3]/td[2]').text
except:
    pass

try:
    vehicleClass = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[4]/td[2]').text
except:
    pass

try:
    fuelType = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[4]/td[4]').text
except:
    pass

try:
    makerOrModel = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[5]/td[2]').text
except:
    pass

try:
    fitnessUpto = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[6]/td[2]').text
except:
    pass

try:
    insuranceUpto = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[6]/td[4]').text
except:
    pass

try:
    fuelNorms = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[7]/td[2]').text
except:
    pass

try:
    roadTaxPaidUpto = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[7]/td[4]').text
except:
    pass

try:
    nocDetails = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt64"]/table/tbody/tr[8]/td[2]').text
except:
    pass

print(registrationNumber)
print(registrationDate)
print(chassisNumber)
print(engineNumber)
print(ownerName)
print(vehicleClass)
print(fuelType)
print(makerOrModel)
print(fitnessUpto)
print(insuranceUpto)
print(fuelNorms)
print(roadTaxPaidUpto)
print(nocDetails)
