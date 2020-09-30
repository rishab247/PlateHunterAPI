from flask import Flask, jsonify, request, make_response, logging, g
import json
import atexit
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data import dataclass as data
# data = datad()
# from selenium import webdriver
import base64
import urllib.request
# import time
import os
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
# from selenium.webdriver.chrome.options import Options
#
#
# app = Flask(__name__)
#
#
#
# # @app.route('/start', methods=['POST'])
# # def start():
# #
# #     # starting time
# #     start = time.time()
# #
# #     print(time.time() - start)
# #     browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
# #     print(time.time() - start)
# #     plateNumber = ""
# #     captchaAnswer = ""
# #
# #     # captcha selector tag : //*[@id="form_rcdl:j_idt32:j_idt37"]
# #
# #     browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
# #     browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
# #     browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys(captchaAnswer)
# #     print(time.time() - start)
# #
# #     # browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').
# #     img = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').get_attribute('src')
# #     print(img)
# #     print(time.time() - start)
# #     urllib.request.urlretrieve(img, "captcha.png")
# #     z = base64.b64encode(urllib.request.urlopen(img).read())
# #     # print(sys. getsizeof(browser))
# #     return jsonify({'msg': str(z)}), 200
# #
# #
#
#
#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('--no-proxy-server')
# chrome_options.add_argument("--proxy-server='direct://'")
# chrome_options.add_argument("--proxy-bypass-list=*")
# @app.route('/verify', methods=['POST'])
# def verify():
#     try:
#         chrome_options.add_argument('headless')
#         print(os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver.exe'))
#         browser = webdriver.Chrome(options=chrome_options, executable_path=os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver.exe'))
#         app.logger.info('test4')
#         # starting time
#         start = time.time()
#
#         app.logger.info('test5')
#         print(time.time() - start)
#         browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
#         print(time.time() - start)
#         plateNumber = ""
#         captchaAnswer = ""
#
#         app.logger.info('test6')
#         # captcha selector tag : //*[@id="form_rcdl:j_idt32:j_idt37"]
#
#         browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
#         browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
#         browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys(captchaAnswer)
#         print(time.time() - start)
#
#         app.logger.info('test6')
#         # browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').
#         img = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').get_attribute('src')
#         print(img)
#         print(time.time() - start)
#         urllib.request.urlretrieve(img, "captcha.png")
#         z = base64.b64encode(urllib.request.urlopen(img).read())
#         # print(sys. getsizeof(browser))
#         return jsonify({'msg': str(z[2:-1])}), 200
#     except Exception as e :
#         return jsonify({'msg': str(e),"path":str(os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver.exe'))}), 200
#
#
# @app.route('/getdetails', methods=['POST'])
# def getdetails():
#     app.logger.info('test2')
#     jsondata = request.get_data().decode("utf-8")
#     jsondata = json.loads(jsondata)
#
#     return jsonify({'msg': jsondata['code']}), 200
# @app.route('/')
# def About():
#     app.logger.info('test1')
#     return jsonify({'About': 'STUFFFF'}), 200
#
#
#
#
# if __name__ == '__main__':
#
#     app.run(debug=True)

from selenium import webdriver
# from flask import Flask
from selenium.webdriver.chrome.options import Options




app = Flask(__name__)
dic = {}

@app.route('/',methods=['POST'])
def getcaption(  ):
    if (data.id == 2):
        data.id = 0
    try:

        json_data = request.json
        plateNumber = json_data['nameplateno']
    except:
        return jsonify({'msg': "Wrong Format"}), 500


    try:
         # browser = webdriver.Chrome(options=chrome_options)
        # global browser
        print( data.id )
        # print(data.store[data.id])
        # print(2)
        # print(2)
        try:
            browser = data.store[data.id]

            browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
        except:
            print('break')
            browser = data.new(data)
            browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')

        # print(3)

        browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
        browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
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


        # print(1)
        # browser.quit()
        data.store[data.id] = browser

        # data.id+=1
        if(data.id==2):
            data.id = 1
        else:
            data.id += 1
        print((data.id))
         # dic[xxx.id] = browser
        # browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys("ans")
        # browser.find_element_by_class_name("ui-button-text").click()
        return jsonify({ 'msg' : str(img_captcha_base64)[1:] , 'id' : str(data.id-1)}),200
    except Exception as e :
            return jsonify({'msg': 'error: '+ str(e)}), 500


@app.route('/getdata',methods=['POST'])
def getdata():
    # print(data.store)
    try:
        json_data = request.json
        a_value = int(json_data["id"])
    except Exception as e :
        return jsonify({'msg': "Wrong Format"}), 500


    try:
        ans =  str(json_data["ans"])
        print( ans)
        if (a_value < 0 or a_value > 100):
            raise Exception("Wronge id")

        if (data.store[a_value] == 0):
            raise Exception("Wronge id")

        if (ans == ""):
            raise Exception("Wronge ans")

        # global browser
        print(a_value)
        browser = data.store[a_value]
        print(browser.title)

        browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt35:CaptchaID"]').send_keys(ans)
        browser.find_element_by_class_name("ui-button-text").click()

        try:
            time.sleep(0.3)
            browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt14"]/div')
            raise  Exception('Invalid Captcha!')
        except:
            print("pass")
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
            x = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[1]/td[2]')))
        except TimeoutException:
            raise  Exception('Invalid Car Number Plate!')

        except:
            raise  Exception('An Error Occurred!')

        try:
            registrationNumber = browser.find_element_by_xpath(
                '//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[1]/td[2]').text
        except:
            pass

        try:
            registrationDate = browser.find_element_by_xpath(
                '//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[1]/td[4]').text
        except:
            pass

        try:
            chassisNumber = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[2]/td[2]').text
        except:
            pass

        try:
            engineNumber = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[2]/td[4]').text
        except:
            pass

        try:
            ownerName = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[3]/td[2]').text
        except:
            pass

        try:
            vehicleClass = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[4]/td[2]').text
        except:
            pass

        try:
            fuelType = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[4]/td[4]').text
        except:
            pass

        try:
            makerOrModel = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[5]/td[2]').text
        except:
            pass

        try:
            fitnessUpto = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[6]/td[2]').text
        except:
            pass

        try:
            insuranceUpto = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[6]/td[4]').text
        except:
            pass

        try:
            fuelNorms = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[7]/td[2]').text
        except:
            pass

        try:
            roadTaxPaidUpto = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[7]/td[4]').text
        except:
            pass

        try:
            nocDetails = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt66"]/table/tbody/tr[8]/td[2]').text
        except:
            pass

        # data.store[a_value].close()
        # data.store[a_value] = 0

        return jsonify({'msg': str(a_value),
                        'registrationNumber':registrationNumber,
                        'registrationDate':registrationDate,
                        'chassisNumber':chassisNumber,
                        'engineNumber':engineNumber,
                        'ownerName':ownerName,
                        'makerOrModel':makerOrModel,
                        'vehicleClass':vehicleClass,
                        'fuelType':fuelType,
                        'fitnessUpto':fitnessUpto,
                        'insuranceUpto':insuranceUpto,
                        'fuelNorms':fuelNorms,
                        'roadTaxPaidUpto':roadTaxPaidUpto,
                        'nocDetails':nocDetails
                        }), 200
    except Exception as e :
        # try:
        #     data.store[a_value].close()
        # except:
        #     pass

        # data.store[a_value] = 0
        return jsonify({'msg': str(e)}), 500
def shutdownlitener():

    for i in range(4):
        try:
            data.store[i].close()
        except:
            pass



if __name__ == '__main__':

    for i in range(2):
        data.store[i] = data.new(data)
    # print(data.store)
    # print(dic)
    # chrome_options = Options()
    # # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('--no-proxy-server')
    # chrome_options.add_argument("--proxy-server='direct://'")
    # chrome_options.add_argument("--proxy-bypass-list=*")
    # # gdd = ChromeDriverManager()
    # # gdd.download_and_install()
    # #         chrome_options.binary_location = GOOGLE_CHROME_PATH
    # print(os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver.exe'))
    # browser = webdriver.Chrome(options=chrome_options)
    atexit.register(shutdownlitener)

    app.run(debug=True)
