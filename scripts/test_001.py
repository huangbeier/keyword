# @Author ：黄贝尔
# @Time ：2021/5/7__14:08
# #coding:utf-8
from config.config import excelpath, auth_code, reportpath
from action.eleAction import *
from utils.send_mail import SendMail
from utils.exceltools import Excel_tools
from utils.logg import Loggings
log=Loggings()
ex=Excel_tools()
ex.read_work_book(excelpath)


def test_run():
    try:
        ex.read_work_sheet('测试用例')
        row_nums=ex.get_max_rows()
        mail = SendMail('smtp.163.com')
        send_address = "beier0917@163.com"
        send_password = auth_code
        receive_address = ['953564459@qq.com']
        title = "测试报告"
        for i in range(2,row_nums+1):

            ex.read_work_sheet('测试用例')
            info=ex.get_specific_data(i,5)
            if info=='y':
                case_step_page=ex.get_specific_data(i,4)
                ex.read_work_sheet(case_step_page)
                step_nums=ex.get_max_rows()
                for j in range(2, step_nums + 1):

                    case =ex.get_row_data(j)
                    case_id=case[0]
                    case_step=case[1]
                    case_keyword=case[2]
                    case_ele_type=case[3]
                    case_ele_value=case[4]
                    case_value=case[5]

                    expression=''
                    if 'assert' in case_keyword:
                        expression=case_keyword+'('+str(i)+',"'+case_value+'")'
                        # print(expression)
                    elif case_ele_type is None and case_ele_value is None and case_value:
                        if isinstance(case_value,int):
                            expression=case_keyword+'('+str(case_value)+')'
                        else:
                            expression = case_keyword + '("' + case_value + '")'
                        #print(expression)
                    elif case_ele_type is None and case_ele_value is None and case_value is None:
                        expression=case_keyword+'()'
                        #print(expression)
                    elif case_ele_type and case_ele_value and case_value is None:
                        expression=case_keyword+'("'+case_ele_type+'","'+case_ele_value+'")'
                        #print(expression)
                    elif case_ele_type and case_ele_value and case_value :
                        if isinstance(case_value, int):
                            expression = case_keyword + '("' + case_ele_type + '","' + case_ele_value + '",'+str(case_value)+')'
                        else:
                            expression = case_keyword + '("' + case_ele_type + '","' + case_ele_value + '","' + case_value + '")'
                        #print(expression)

                    eval(expression)

        content = mail.get_content()
        mail.send_mail(send_address, send_password, receive_address, title, content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test_run()