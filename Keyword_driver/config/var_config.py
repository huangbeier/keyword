'''
常用变量配置文件
'''
import os

parent_dir_path = os.path.dirname(os.path.dirname(__file__))



# 测试数据路径
testDataPath = os.path.join(parent_dir_path, u'testdata\\163邮箱发送邮件.xlsx')

print(testDataPath)


# chrome 驱动路径
chorme_dirver_path = os.path.join(parent_dir_path, u'chromedriver.exe')


# firefox 驱动路径
firefox_dirver_path = ""


# ie 驱动路径
ie_dirver_path = ""
