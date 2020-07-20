# encoding=utf-8
# python:2.7.x
import sys
import copy
import os
import time
from urllib import unquote
from urllib import quote
import re
from lxml import etree
import json
import HTMLParser
reload(sys)
sys.setdefaultencoding('utf8')
ALL_Info={
    'firstname':"",
    'lastname' :"",
    'address'  :"",
    'work'     :{},
}


def decodeHtml(input):
    h = HTMLParser.HTMLParser()
    s = h.unescape(input)
    return s
def newparse(content,fi):
    worklist=[]
    content = unquote(content).replace('&quot;', '"')
#    print "开始解析"
#    print content
#    try:
#    print type(content)
#    content = content.decode()
#    except UnicodeDecodeError:
#        print "contern decode erro"

    profile_txt =re.findall(r'"included":.{"pag.*]',content,re.M)  #根据数据格式只匹配一次
#    print '匹配后文本'
    if profile_txt:
        profile_txt[0] = '{'+profile_txt[0]+'}'
    else:
        return 1
#try:
#    load = json.loads(profile_txt[0])
#except ValueError:
    try:
        profile_txt[0] = decodeHtml(profile_txt[0])
    except UnicodeDecodeError:
        return 1 
    load = json.loads(profile_txt[0])
    

    inlist = load['included']    #include 解析后为List
    for i in inlist:
        if( i.has_key('multiLocaleLastName')):
            ALL_Info['firstname']= json.dumps(i['multiLocaleLastName'], encoding="UTF-8", ensure_ascii=False)
        if( i.has_key('multiLocaleFirstName')):
            ALL_Info['lastname'] = json.dumps(i['multiLocaleFirstName'], encoding="UTF-8", ensure_ascii=False)
        if(i.has_key('defaultLocalizedNameWithoutCountryName')):
            ALL_Info['address'] = json.dumps(i['defaultLocalizedNameWithoutCountryName'], encoding="UTF-8", ensure_ascii=False)
    
        if(i.has_key('dateRange') and not i.has_key('*profilePositionInPositionGroup')):
            if(i.has_key('companyName')):
                Work_Info={}
                worktime = ''
                worktitle = ''
                
                if(i['dateRange'].has_key('end')):
                    if(i['dateRange']['start'].has_key('month') and i['dateRange']['end'].has_key('month')):
                        worktime = i['dateRange']['start']['year'],'.',i['dateRange']['start']['month'],'-',i['dateRange']['end']['year'],',',i['dateRange']['end']['month']
                    else:                   
                        worktime = i['dateRange']['start']['year'],'-',i['dateRange']['end']['year']
                else:
                    if(i['dateRange']['start'].has_key('month')):
                        worktime = i['dateRange']['start']['year'],'.',i['dateRange']['start']['month'] ,'-', "now"
                    else:
                        worktime = i['dateRange']['start']['year'],'-', "now"
                try:
                    worktitle = i['title']
                except KeyError:
                    worktitle = ''
                Work_Info['worktitle'] =worktitle
                Work_Info['worktime'] =worktime
                
                Work_Info['workcompanyname'] =i['companyName']
                worklist.append(Work_Info)
    fi.write("/------------------------------------------------\r\n") 
    fi.write('姓：'+ ALL_Info['firstname']+'\r\n')
    fi.write('名：'+ ALL_Info['lastname']+'\r\n')
    fi.write('地区: '+ ALL_Info['address']+'\r\n')
    fi.write('\r\n')
    fi.write("工作经验："+'\r\n')
    print '姓：'+ ALL_Info['firstname']
    print '名：'+ ALL_Info['lastname']
    print '地区：'+ALL_Info['address']
    print ""
    print "工作经验："
    for i in worklist:
        fi.write('   公司名称：' + i['workcompanyname']+'\r\n')
        fi.write('   工作岗位：'+i['worktitle']+'\r\n')
        print '公司名称：',i['workcompanyname']
        print '工作岗位：',i['worktitle']
        time = ""
        for k in i['worktime']:
            if(k == '-'):
                k = ' - '
            time += str(k)
        fi.write('   工作时间：'+time+'\r\n')
        fi.write("\r\n")
        print '工作时间：',time
        print ""
    fi.write("------------------------------------------------/\r\n\r\n") 
        

def get_company_name():
    s_http="http"
    fi = open("allurl.txt",'r')
    company_file = open("company.txt",'w')
    for name in fi:
        if(name.find(s_http)):
            company_file.write(name)
            
def oneNum_to_threeNum(num):
    n=str(num)
    s = n.zfill(3)
    return s
if __name__ == '__main__':
#    get_company_name()
    html_path = "../Linked_HTML/"
    dirs = os.listdir( html_path )
    company_file = open("company.txt",'r')
    result_file = open('result.txt','w')
    company_num = 0;
    for company_name in company_file:
        result_file.write(company_name+'\n')            #write company name to result.txt
        company_num += 1
        str_num = oneNum_to_threeNum( company_num )     #get tog str_num
        re_str = '.*' + str_num + '.*'                  #re str
#        print re_str
        for name in dirs:
            html_name = re.findall(re_str,name)
            for  name in html_name:
                html_file = open(html_path+name,'r')
#                result_file.write(html_path+name+'\n')
                html_content = html_file.read()
                parse_ret = newparse(html_content,result_file)
                html_file.close()
                if parse_ret != 1:
                    os.remove(html_path+name)
                    pass
#                    
#               for h in html_file:
#                   print h
#           print 'ttttt' , type(test)
#           test = ''.join(test)                        #str
#           test = test + '\r\n'
#           print type(test)
#            if test != '':
#                print test
#                test_file.write(test)