from selenium import webdriver
browser = webdriver.PhantomJS()
# browser.set_window_size(1120, 550)
# driver.get("https://duckduckgo.com/")
# driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
# driver.find_element_by_id("search_button_homepage").click()
# print(driver.current_url)
# driver.quit()

browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')

# print(3)

browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys('12343232')
browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys("2133")
captcha = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt35:j_idt40"]')
# print(4)
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

print(img_captcha_base64)
