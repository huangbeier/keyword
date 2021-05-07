from selenium.webdriver.support.wait import WebDriverWait



def find_element(driver, find_type, expression):
    '''
    查找元素
    :param driver:
    :param find_type:
    :param expression:
    :return:
    '''
    # element = driver.find_element(by=find_type, value=expression)
    # return element
    try:
        element = WebDriverWait(driver,20).until(lambda driver:driver.find_element(by=find_type, value=expression))
        return element
    except Exception as e:
        print(e)


def find_elements(driver, find_type,expression):
    '''
    查找元素组（多个元素）
    :param driver:
    :param find_type:
    :param expression:
    :return:
    '''
    try:
        elements = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(by=find_type, value=expression))
        return elements
    except Exception as e:
        print(e)
