# Python:2.7.x
import os
import time
import win32api
import win32con
import webbrowser
import win32con
import random
VK_CODE = {
  'backspace':0x08, 'tab':0x09,         'clear':0x0C,       'enter':0x0D,       'shift':0x10, 'ctrl':0x11,
  'alt':0x12,       'pause':0x13,       'caps_lock':0x14,   'esc':0x1B,         'spacebar':0x20,
  'page_up':0x21,   'page_down':0x22,   'end':0x23,
  'home':0x24,
  'left_arrow':0x25,
  'up_arrow':0x26,
  'right_arrow':0x27,
  'down_arrow':0x28,
  'select':0x29,
  'print':0x2A,
  'execute':0x2B,
  'print_screen':0x2C,
  'ins':0x2D,
  'del':0x2E,
  'help':0x2F,
  '0':0x30,
  '1':0x31,
  '2':0x32,
  '3':0x33,
  '4':0x34,
  '5':0x35,
  '6':0x36,
  '7':0x37,
  '8':0x38,
  '9':0x39,
  'a':0x41,
  'b':0x42,
  'c':0x43,
  'd':0x44,
  'e':0x45,
  'f':0x46,
  'g':0x47,
  'h':0x48,
  'i':0x49,
  'j':0x4A,
  'k':0x4B,
  'l':0x4C,
  'm':0x4D,
  'n':0x4E,
  'o':0x4F,
  'p':0x50,
  'q':0x51,
  'r':0x52,
  's':0x53,
  't':0x54,
  'u':0x55,
  'v':0x56,
  'w':0x57,
  'x':0x58,
  'y':0x59,
  'z':0x5A,
  'numpad_0':0x60,
  'numpad_1':0x61,
  'numpad_2':0x62,
  'numpad_3':0x63,
  'numpad_4':0x64,
  'numpad_5':0x65,
  'numpad_6':0x66,
  'numpad_7':0x67,
  'numpad_8':0x68,
  'numpad_9':0x69,
  'multiply_key':0x6A,
  'add_key':0x6B,
  'separator_key':0x6C,
  'subtract_key':0x6D,
  'decimal_key':0x6E,
  'divide_key':0x6F,
  'F1':0x70,
  'F2':0x71,
  'F3':0x72,
  'F4':0x73,
  'F5':0x74,
  'F6':0x75,
  'F7':0x76,
  'F8':0x77,
  'F9':0x78,
  'F10':0x79,
  'F11':0x7A,
  'F12':0x7B,
  'F13':0x7C,
  'F14':0x7D,
  'F15':0x7E,
  'F16':0x7F,
  'F17':0x80,
  'F18':0x81,
  'F19':0x82,
  'F20':0x83,
  'F21':0x84,
  'F22':0x85,
  'F23':0x86,
  'F24':0x87,
  'num_lock':0x90,
  'scroll_lock':0x91,
  'left_shift':0xA0,
  'right_shift ':0xA1,
  'left_control':0xA2,
  'right_control':0xA3,
  'left_menu':0xA4,
  'right_menu':0xA5,
  'browser_back':0xA6,
  'browser_forward':0xA7,
  'browser_refresh':0xA8,
  'browser_stop':0xA9,
  'browser_search':0xAA,
  'browser_favorites':0xAB,
  'browser_start_and_home':0xAC,
  'volume_mute':0xAD,
  'volume_Down':0xAE,
  'volume_up':0xAF,
  'next_track':0xB0,
  'previous_track':0xB1,
  'stop_media':0xB2,
  'play/pause_media':0xB3,
  'start_mail':0xB4,
  'select_media':0xB5,
  'start_application_1':0xB6,
  'start_application_2':0xB7,
  'attn_key':0xF6,
  'crsel_key':0xF7,
  'exsel_key':0xF8,
  'play_key':0xFA,
  'zoom_key':0xFB,
  'clear_key':0xFE,
  '+':0xBB,
  ',':0xBC,
  '-':0xBD,
  '.':0xBE,
  '/':0xBF,
  ';':0xBA,
  '[':0xDB,
  '\\':0xDC,
  ']':0xDD,
  "'":0xDE,
  '`':0xC0}
def one_key_updown(key):
    win32api.keybd_event(key,0,0,0)     # enter
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)
def one_key_up_delay_down(key,delay):
    win32api.keybd_event(key,0,0,0)     # enter
    time.sleep(delay)
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)
def two_key_updown(key1,key2):
    win32api.keybd_event(key1,0,0,0)     # enter
    win32api.keybd_event(key2,0,0,0)     # enter
    win32api.keybd_event(key1,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(key2,0,win32con.KEYEVENTF_KEYUP,0)
def alt_tab():
    #change tab
    win32api.keybd_event(18,0,0,0)     # enter
    win32api.keybd_event(9,0,0,0)     # enter
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)
def ctrl_s():
    #ctrl + s
    win32api.keybd_event(17,0,0,0)     # enter
    win32api.keybd_event(83,0,0,0)     # enter
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
def Left_Arrow():
    win32api.keybd_event(37,0,0,0)     # enter
    win32api.keybd_event(37,0,win32con.KEYEVENTF_KEYUP,0)
def enter():
    # enter
    win32api.keybd_event(13,0,0,0)    
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
def rename_html(num_list):
    one_key_updown(VK_CODE['right_arrow'])
    one_key_updown(VK_CODE['-'])
    one_key_updown(0x30 + num_list[0])
    one_key_updown(0x30 + num_list[1])
    one_key_updown(0x30 + num_list[2])
    time.sleep(0.5)
def save_html(cmp_num):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
    for i in range(random.randint(8,20)):
        one_key_up_delay_down(VK_CODE['down_arrow'],0.2)
#        one_key_updown(VK_CODE['down_arrow'])
    time.sleep(random.randint(1,4))
    for i in range(random.randint(1,20)):
        one_key_up_delay_down(VK_CODE['up_arrow'],0.2)
        
    time.sleep(1)
    two_key_updown(VK_CODE['ctrl'],VK_CODE['s'])
    time.sleep(3)
    num_list = get_comany_num_key(cmp_num)
    rename_html(num_list)
    enter()
    time.sleep(2)
    one_key_updown(VK_CODE['left_arrow'])
    time.sleep(1.5)
    enter()
    time.sleep(random.randint(2,8))
#    print "crtl w"
    two_key_updown(VK_CODE['ctrl'],VK_CODE['w'])
    time.sleep(random.randint(1,3))
    
def open_url(cmp_num,url):
 #   print 'open_url'
    webbrowser.open(url)
    time.sleep(7)
    save_html(cmp_num)
    

def get_comany_num_key(cmp_num):
    ge = cmp_num % 10
    temp = cmp_num / 10
    shi =temp % 10
    bai = cmp_num / 100
    res = [bai,shi,ge]
    return res
def check_geted_url(tog_url):
    res = 0
    getoverurl = open('getoverurl.txt','a+')
    for url in getoverurl:
        if url == tog_url:
            res = 1
    getoverurl.close()
    return res
if __name__=='__main__':
    comany_num = 0
    open_time = 0
    long_time = 0
    time_now = 0
    urlall = open('allurl.txt','r')
    get_over_url = open('getoverurl.txt','a+')
    s_http = 'http'
    for url in get_over_url:
        if(url.find(s_http)):
            comany_num += 1
    nodo = 0
    for url in urlall:
        if not (check_geted_url(url)):
            get_over_url.write(url)
            if(url.find(s_http)):
                print url
                comany_num += 1
            else:
                time_now += 1
                open_time+=1
                long_time += 1
                open_url(comany_num,url)
                if(open_time == 9):
                    print "enter sleep"
                    print time_now
                    open_time = 0
                    time.sleep(random.randint(60,200))
                if(long_time == 80):
                    print "enter sleep2"
                    long_time = 0
                    open_time = 0
                    time.sleep(random.randint(240,500))
    get_over_url.close()
    urlall.close()


#    t = 100
#    for i in range(1):
#        webbrowser.open("https://www.cnblogs.com/cola-1998/p/10807518.html")

