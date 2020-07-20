# Python:2.7.x
# encoding=utf-8
import sys
import copy
import os
import time
import re
import json
reload(sys)
sys.setdefaultencoding('utf8')

def searchKeyWorld(key):
    result_file = open("result.txt",'r')
    content_list = []
    record = False
    bingo = False
    num = 0
    for result_line in result_file:
        if(result_line == "/------------------------------------------------\r\n"):
#            print "Beg"
            record = True
            continue
        if(result_line == "------------------------------------------------/\r\n"):
#            print "End"
            if(bingo == True):
                num +=1
                new_file.write(str(num)+'\n')
                for i in content_list:
                    new_file.write(i)
            content_list = []
            record = False
            bingo = False
            continue
        if(record == True):
            content_list.append(result_line)
            resre = re.findall(key,result_line,re.M)
#            print resre
            if resre:
                bingo = True
    print("Sum Result:",num)
    print("Result Save at \"./SearchResult.txt\"")

if __name__ == '__main__':
    company_file = open("company.txt",'r')
    new_file = open('SearchResult.txt','w')
    i = 0
    for company_name in company_file:
        new_file.write(company_name+'\r\n')
        searchKeyWorld(company_name.strip().strip(':'))
    new_file.close()
    company_file.close()
        