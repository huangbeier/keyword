# @Author ：黄贝尔
# @Time ：2021/5/7__11:21
# #coding:utf-8
import traceback
from utils.exceltools import Excel_tools
from selenium import webdriver
from config.config import Chromepath, excelpath
from utils.logg import Loggings
import time
from utils.find_element import find_element, find_elements

log=Loggings()
driver=None
def open_browser(driver_name,*args):
    global driver
    if driver_name.lower()=='chrome':
        driver=webdriver.Chrome(Chromepath)
    else:
        print('找不到浏览器驱动')

def get_url(url,*args):
    try:
        driver.get(url)
    except Exception as e:
        print(e)

def max_window():
    try:
        driver.maximize_window()
    except Exception as e:
        print(e)

def sleep(seconds,*args):
    time.sleep(seconds)

def switch_frame(ele_type,ele_vaule,*args):
    try:
        i_frame=find_element(driver,ele_type,ele_vaule)
        driver.switch_to.frame(i_frame)
    except Exception as e:
        print(e)

def input_content(ele_type,ele_vaule,values,*args):
    try:
        find_element(driver, ele_type, ele_vaule).send_keys(values)
    except Exception as e:
        print(e)

def click(ele_type,ele_vaule,*args):
    try:
        find_element(driver, ele_type, ele_vaule).click()
    except Exception as e:
        print(e)

def assert_title(row,values,*args):
    ex=Excel_tools()
    ex.read_work_book(excelpath)
    ex.read_work_sheet('测试用例')
    try:
        assert values in driver.title
        ex.write_specific_data(row, 6, 'pass')
    except Exception as e:
        ex.write_specific_data(row, 6, 'fail')
        log.error(f'第{str(row)}行用例断言错误\r\n'+traceback.format_exc())
        print(e)

def input_subject(ele_type,ele_vaule,values,*args):
    try:
        a,b=ele_vaule.split(',')
        find_elements(driver,ele_type,a)[int(b)].send_keys(values)
    except Exception as e:
        print(e)

def switch_default(*args):
    try:
        driver.switch_to.default_content()
    except Exception as e:
        print(e)

def assert_pagesource(row,values,*args):
    ex=Excel_tools()
    ex.read_work_book(excelpath)
    ex.read_work_sheet('测试用例')
    try:
        assert values in driver.page_source
        ex.write_specific_data(row, 6, 'pass')
    except Exception as e:
        ex.write_specific_data(row, 6, 'fail')
        log.error(f'第{str(row)}行用例断言错误\r\n'+traceback.format_exc())

        print(e)

def close_browser():
    driver.quit()


if __name__ == '__main__':
    input_subject('class name','nui-ipt-input,2','cctester')




