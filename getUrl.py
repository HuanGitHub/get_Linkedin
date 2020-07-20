# encoding=utf-8
# ----------------------------------------
# Python：2.7
# ----------------------------------------
import sys
import copy
import os
import time
from urllib import unquote
import requests
from urllib import quote
import re
from lxml import etree
import json

reload(sys)
sys.setdefaultencoding('utf8')

def get_linkedin_url(url):
    try:
        r = requests.get(url, allow_redirects=False)
        if r.status_code == 302 and 'Location' in r.headers.keys() and 'linkedin.com/in/' in r.headers['Location']:
            return r.headers['Location']     #获取重定向后的Url  未使用
    except Exception, e:
        print 'get linkedin url failed: %s' % url
    return ''

def crawl(url):
    """ 抓取每一个搜索结果 """
    print url
    fi = open('allurl.txt','a')
#    url = get_linkedin_url(url)  
    if url != '':
        print url
        fi.write(url+'\r\n')

def once_GetInfo(company_name):
    maxpage = 70 # 抓取前70页百度搜索结果，百度搜索最多显示76页
    # 百度搜索 key world
    url = 'http://www.baidu.com/s?ie=UTF-8&usm=3&rsv_idx=2&rsv_page=1&wd=%20%7C%20领英%20' + quote(company_name) + '%20site%3Alinkedin.com'
    results = []
    failure = 0
    print company_name+':'
    fi = open('allurl.txt','a')
    fi.write(company_name+':'+'\r\n')
    while len(url) > 0 and failure < 10:
        try:
            r = requests.get(url, timeout=19)
        except Exception, e:
            failure += 1
            continue
        print r.status_code
        if r.status_code == 200:
            hrefs = list(set(re.findall('"(http://www\.baidu\.com/link\?url=.*?)"', r.content)))  # 一页有10个搜索结果
            for href in hrefs:
                fi.write(url+'\r\n')
            results += hrefs
            tree = etree.HTML(r.content)
            nextpage_txt = tree.xpath('//div[@id="page"]/a[@class="n" and contains(text(), "下一页")]/@href'.decode('utf8'))
            url = 'http://www.baidu.com' + nextpage_txt[0].strip() if nextpage_txt else ''
            failure = 0
            maxpage -= 1
            if maxpage <= 0:
                break
        else:
            failure += 2
            print 'search failed: %s' % r.status_code
    if failure >= 10:
        print 'search failed: %s' % url
    fi.close()
if __name__ == '__main__':
    if os.path.isfile('allurl.txt'):
        os.remove('allurl.txt')
    fi = open('company.txt','r')
    for line in fi:
        ln = line.strip('\r\n')
        once_GetInfo(ln)
        
