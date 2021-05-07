from config.var_config import testDataPath
from util.ExcelOperate import ExcelOperate
from action.elmentAction import *

excel = ExcelOperate()
excel.load_workbook(testDataPath)



def test_run():
    try:
        excel.get_sheet_by_name("测试用例")
        row_nums = excel.get_rows_nums()
        for i in range(2, row_nums+1):
            # 判断用例是否要执行
            excel.get_sheet_by_name("测试用例")
            if excel.get_cell_vlaue(i,5).lower() == "y":
                case_step_sheet = excel.get_cell_vlaue(i, 4)
                # 读取响应的页
                excel.get_sheet_by_name(case_step_sheet)
                # 拿到步骤数
                step_nums = excel.get_rows_nums()
                for j in range(2, step_nums+1):
                    temp_row_value = excel.get_row_values(j)
                    index = temp_row_value[0]
                    desc  = temp_row_value[1]
                    key_word = temp_row_value[2]
                    location_type = temp_row_value[3]
                    location_express = temp_row_value[4]
                    operate_value = temp_row_value[5]

                    # 构造函数表达式
                    # 定位方式 和 定位表达式为空， 关键字 和 操作值不为空，比如 open_browser , get_url, sleep ,assert_title
                    method_express = ''
                    if key_word and operate_value and location_type is None and location_express is None:
                        # 判断操作值是否是整数，如果是，注意拼接方式
                        if isinstance(operate_value,int):
                            method_express = key_word + "(" + str(operate_value) + ")"
                        else:
                            method_express = key_word + "('" + operate_value + "')"
                        print(method_express)

                    # 只有关键字不为空 如 max_window，  close_browser
                    elif  key_word and operate_value is None and location_type is None and location_express is None:
                        method_express = key_word + "()"
                        print(method_express)

                    # 只有操作值为空，switch_frame ，cliclk
                    elif  key_word and operate_value is None and location_express and location_type:
                        method_express = key_word + "('" + location_type +"','" + location_express + "')"
                        print(method_express)

                    # 都不为空 如 input_content
                    elif key_word and operate_value and location_type and location_express:
                        if isinstance(operate_value,int):
                            method_express = key_word + "('" + location_type + "','" + location_express + "'," + str(operate_value) + ")"
                        else:
                            method_express = key_word + "('" + location_type + "','" + location_express + "','" + operate_value + "')"
                        print(method_express)

                    # 通过 eval函数来执行 上面构造的函数表达式
                    eval(method_express)

    except Exception as e:
        print(e)


def func1():
    print('it is func1')

if __name__ == '__main__':
    test_run()
    # 将传入的字符创 当做一个表达式来求值，并返回结果
    # print(eval("2+2"))
    # print(eval("1==1"))
    # print(eval("1==2"))
    # eval('func1()')