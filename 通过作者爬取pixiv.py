from selenium import webdriver
import time
import os
import subprocess
import base64
from lxml import etree

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

driver = webdriver.Chrome(chrome_options=chrome_options)
thunder_path = 'D:/Thunder/Program/Thunder.exe'


def Url2Thunder(url):
    url = 'AA' + url + 'ZZ'
    url = base64.b64encode(url.encode('ascii'))
    url = b'thunder://' + url
    thunder_url = url.decode()
    return thunder_url


#
# def download_with_thunder(file_url):
#     subprocess.call([thunder_path, file_url])

idurl = input("please enter the author's id：")
img_url = []
for i in range(1, 8):
    driver.get("https://www.pixiv.net/member_illust.php?id=" + idurl + "&p=%d" % i)
    flag = input("enter sth after your login:")
    time.sleep(5)
    # print(driver.page_source)
    page = driver.page_source
    dom = etree.HTML(page)
    time.sleep(2)
    ids = dom.xpath('//img[contains(@src,"")]/@src')
    # print(ids)

    for id in ids:
        # print(id)
        if ('250x250' in id) == True:
            date_id = id.strip('https://i.pximg.net/c/250x250_80_a2/')
            date_id = date_id.strip('square1200.jpg')
            # print(date_id)
            img_url_temp = 'https://i.pximg.net/img' + date_id + 'master1200.jpg'
            turl = Url2Thunder(img_url_temp)
            img_url.append(turl)
            time.sleep(2)

    for i in img_url:
        # download_with_thunder(img_url)  # 直接request.get的话会403
        time.sleep(5)
        print(i)
    img_url = []
    print("one page accomplished")
    time.sleep(5)
