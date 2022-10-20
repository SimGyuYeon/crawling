import io
import sys
import time
import urllib.request as req
# from sqlalchemy import create_engine
import requests
from bs4 import BeautifulSoup
import pandas as pd
# import pymysql
from fake_useragent import UserAgent
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
import logging
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GetNews:

    cnt_list = 0
    cnt_err = 0
    htmlContent = '<ul class="news">'

    def get_news(self, url, set_day):
        ua = UserAgent()
        # 헤더 선언
        headers = {
            'User-Agent': ua.ie,
            'referer': 'https://sports.news.naver.com'
        }

        try:
            driver = webdriver.Chrome()
            driver.get(url)

            # headlines = driver.find_elements(By.CLASS_NAME, 'headline_item')
            # for items in headlines:
            #     items.find_element(By.CLASS_NAME, "link_headline").click()
            #     print(items.tag_name)
            #     print(items.text)
            # html = driver.page_source

            html = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
            # print('html', html)
            soup = BeautifulSoup(html, 'html.parser')
            # print(soup)
            # content = soup.find("div", attrs={"id":"content"}).find("div", attrs={"class":"headline_list"})
            content = soup.find("div", attrs={"class": "home_news"})
            # print(content)
            list = content.find_all("li")
            for li in list:
                # 추천뉴스 목록
                # print(li)
                # 추천뉴스 제목
                title = li.span.get_text()
                if (title.find('KIA') != -1) | (title.find('kia') != -1) \
                        | (title.find('Kia') != -1) | (title.find('기아') != -1) \
                        | (title.find('키움') != -1):
                    # print(li.a["href"])
                    driver.get(headers['referer'] + li.a["href"])
                    self.cnt_list = self.cnt_list + 1
                    self.htmlContent = self.htmlContent + str(li)
                    time.sleep(1)

            self.htmlContent = self.htmlContent + '</ul>'

        except Exception as err:
            _err = 'Date:' + set_day + '==> error occurred:' + err
            self.cnt_other_err = self.cnt_err + 1

        _err_msg = 'Total news count:' + str(self.cnt_list) + ', Error count:' + str(self.cnt_err)
        print(_err_msg)

        return self.htmlContent

    def getRest(self, url):
        today = str((datetime.today()).strftime("%Y%m%d"))
        msg = self.get_news(url, today)
        return msg

# 블로그 포스팅 함수
def postBlogAPI(title, content):
    url = 'https://www.tistory.com/apis/post/write?'

    param = {
        'access_token':'479630ae6cbc3902c835b167b723877f_ea84b113389aebe34341420875e8590b',
        'blogName':'arg-dev',
        'title':title,
        'content':content,
        'visibility':'0',
        'category':'0',
        'tag':'tag',
        'acceptComment':'1',
        'password':'2693'
    }

    response = requests.post(url, params=param)
    print(response.text)

getNews = GetNews()
msg = getNews.getRest('https://sports.news.naver.com/kbaseball/index')
print(msg)
postBlogAPI(str((datetime.today()).strftime("%Y.%m.%d")) + ' 기아 뉴스', msg)