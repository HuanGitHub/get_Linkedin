#Python V：3.7.x
import sys
import copy
import os
import time
import chardet
import re
import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class InputdialogDemo(QWidget):
    def __init__(self,parent=None):
        super(InputdialogDemo,self).__init__(parent)
        layout=QFormLayout()

        self.btn2=QPushButton("请输入公司名称")
        self.le2=QLineEdit()
        self.le2.setTextMargins(0, 0, 100, 0)
        layout.addRow(self.btn2,self.le2)
        self.btn3=QPushButton("Search")
        self.btn3.setFixedSize(400,40)
        self.btn3.clicked.connect(self.getText)
        layout.addRow(self.btn3)
        
        self.setLayout(layout)
        self.setWindowTitle("根据公司名称获取信息")

    def transGbk2Unicode(self,str_v):
        str_s = str_v.replace(r'%', r'\x')
        res = eval(repr(str_s).replace('\\\\', '\\'))
        return res.decode('gb2312')
    
    def getText(self):
        print(type(self.le2.text()))
        con = self.le2.text()
        con = con.encode("utf-8")
#        print (type(con))
        con = con.decode(encoding="utf-8", errors="strict")
#        print (type(con))
#        ke = self.transGbk2Unicode(self.le2.text())
        self.searchKeyWorld(con)
        
    def searchKeyWorld(self,key):
        result_file = open("result.txt",'r',encoding='UTF-8')
        new_file = open('SearchResult.txt','w',encoding='UTF-8')       #file stly Utf-8
        content_list = []
        record = False
        bingo = False
        num = 0
        for result_line in result_file:
            if(result_line == '/------------------------------------------------\n'):
 #               print("Beg")
                record = True
                continue
            if(result_line == '------------------------------------------------/\n'):
#                print ("End")
                if(bingo == True):
                    num +=1
                    new_file.write(str(num)+'\n')
                    for i in content_list:
                        print(i)
                        new_file.write(i)
                content_list = []
                record = False
                bingo = False
                continue
            if(record == True):
                content_list.append(result_line)
                resre = re.findall(key,result_line,re.M)               
                if resre:
                    bingo = True
        print("Sum Result:",num)
        print("Result Save at \"./SearchResult.txt\"")
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    win=InputdialogDemo()
    win.show()
    sys.exit(app.exec_())




#if __name__ == '__main__':
#    company_file = open("company.txt",'r')
#    new_file = open('newResult.txt','w')
#
#    app = QApplication(sys.argv)
#    ex = Example()
#    sys.exit(app.exec_())
#
#    new_file.close()
#    company_file.close()
        