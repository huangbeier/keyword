'''
把我们的测试用例分成了四个部分
测试步骤  Test step: 是一个小的测试步骤的描述 或者测试对象的一个操作说明
测试步骤中的对象  Test Object ： 是指页面对象或者元素， 比如说 用户名输入框...
测试对象执行的动作  Action : 执行的动作   打开浏览器 ，点击按钮，输入文本
测试对象执行的工作需要的数据    ： 对象操作时所需要的值  用户名名  密码


1. 打开浏览器   浏览器   open   chrome/firefox/ie
2. 输入url     浏览器   输入    http://mail.163.com
3. 窗口最大化  窗口    最大化
4. 切换frame   frame   切换
5. 输入用户名  用户名输入框   输入文本    zhangming002
6. 输入密码    密码输入框     输入文本    zmkmzmkm
7. 点击登录按钮  按钮    点击
8. 等待 3秒             sleep
9. 进行断言             assert
'''

from selenium import webdriver
import time
path = r'D:\迅雷下载\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://mail.163.com/')
driver.maximize_window()

iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)
driver.find_element_by_name('email').send_keys('zhangming0032021')
driver.find_element_by_name('password').send_keys('2wsx3edc')
driver.find_element_by_id("dologin").click()
time.sleep(3)
# 写信
driver.find_element_by_xpath('/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]').click()
time.sleep(2)

# 收件人
driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('923770317@qq.com')
# 主题
driver.find_elements_by_class_name('nui-ipt-input')[2].send_keys('test')

#切换frame
i_frame = driver.find_element_by_class_name('APP-editor-iframe')
driver.switch_to.frame(i_frame)
# 输入文本
driver.find_element_by_class_name('nui-scroll').send_keys('hahahaha')

# 发送
driver.switch_to.default_content()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div/span[2]').click()






