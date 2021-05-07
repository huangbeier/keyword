import time

from selenium import webdriver

from config.var_config import chorme_dirver_path, firefox_dirver_path, ie_dirver_path
from util.find_element import find_element, find_elements

driver = None

def open_browser(browser_name, *args):
    global  driver
    ''' 打开浏览器'''
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(chorme_dirver_path)
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(firefox_dirver_path)
    else:
        driver = webdriver.Ie(ie_dirver_path)


def get_url(url,*args):
    '''访问网址'''
    # global  driver
    try:
        driver.get(url)
    except Exception as e:
        print(e)

def max_window(*args):
    '''窗口最大化'''
    # global driver
    try:
        driver.maximize_window()
    except Exception as e:
        print(e)

def sleep(seconds, *args):
    '''等待seconds '''
    time.sleep(seconds)


def switch_frame(location_type, location_express, *args):
    '''切换frame'''
    # global  driver
    try:
        i_frame= find_element(driver,location_type,location_express)
        driver.switch_to.frame(i_frame)
    except Exception as e:
        print(e)

def input_content(location_type, location_express,content,*args):
    '''输入content'''
    # global  drvier
    try:
        find_element(driver, location_type, location_express).send_keys(content)
    except Exception as e:
        print(e)


def click(location_type,location_express,*args):
    '''点击操作'''
    # global  driver
    try:
        find_element(driver, location_type, location_express).click()
    except Exception as e:
        print(e)


def assert_title(except_value, *args):
    '''断言标题'''
    # global  driver
    try:
        assert except_value in driver.title
    except Exception as e:
        print(e)


def close_browser(*agrs):
    '''关闭浏览器'''
    # global  driver
    try:
        driver.quit()
        driver.quit()
    except Exception as e:
        print(e)


def switch_default(*args):
    '''
    返回默认frame
    :param args:
    :return:
    '''
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        print(e)


def input_subject(location_type, location_express, operate_value,*args):
    '''
    写信，输入主题(得到的是多个控件)
    :param location_type:
    :param location_express:
    :param operate_value:
    :param args:
    :return:
    '''
    global driver
    try:
        location_express, index = location_express.split(',')
        find_elements(driver,location_type,location_express)[int(index)].send_keys(operate_value)
    except Exception as e:
        print(e)

def assert_pagesource(assert_value, *args):
    '''
    断言页面源码 中是否含有 assert_value
    :param assert_value:
    :param args:
    :return:
    '''
    global  driver
    try:
        assert assert_value in driver.page_source
    except Exception as e:
        print(e)




if __name__ == '__main__':
    open_browser('chrome')
    get_url('http://mail.163.com')
    max_window()
    sleep(2)
    switch_frame('tag name', 'iframe')
    input_content('name','email', 'zhangming002')
    input_content('name','password','zmkmzmkm')
    click('id','dologin')
    sleep(2)
    assert_title('网易邮箱6.0版')
    close_browser()





