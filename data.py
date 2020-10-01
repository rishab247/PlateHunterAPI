
from selenium import webdriver
# from flask import Flask
from selenium.webdriver.chrome.options import Options

from flask import Flask, jsonify, request, make_response, logging, g
import json
# from selenium import webdriver
import base64
import urllib.request
# import time
import os
class dataclass:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument('--no-proxy-server')
    # chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--remote-debugging-port=9222")
    # print(os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver.exe'))
    # browser = webdriver.Chrome(options=chrome_options)
    store = {}
    id =0

    def new(self):
        return webdriver.PhantomJS()
