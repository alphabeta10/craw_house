from splinter import Browser
import requests
import random

user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
    (KHTML, like Gecko) Element Browser 5.0', \
    'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
    'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
    Version/6.0 Mobile/10A5355d Safari/8536.25', \
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/28.0.1468.0 Safari/537.36', \
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
def getBrowserHtml(url):
    browser = Browser('chrome', executable_path="D:\\pythonproject\\craw_stock_pro\\chromedriver.exe")
    browser.visit(url)
    html = browser.html
    browser.driver.close()
    return html
def getBrowser(url):
    browser = Browser('chrome', executable_path="D:\\pythonproject\\craw_stock_pro\\chromedriver.exe")
    browser.visit(url)
    return browser
def closeBrowser(browser):
    browser.driver.close()
def getRequestHtml(url):
    try:
        r = random.randint(0, 9)
        headers = {'User-agent': user_agents[r]}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return ""
    except Exception as e:
        print("error of ",e)
        return ""