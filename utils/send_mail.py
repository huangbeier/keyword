# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-04-25
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.config import excelpath, reportpath, auth_code
from utils.exceltools import Excel_tools


class SendMail:
    def __init__(self, mail_host):
        '''
        构建邮件的smtp 服务器的地址
        :param mail_host:
        '''
        self.mail_host = mail_host

    def send(self, title, content, sender, auth_code, receivers):
        '''
        发送该邮件
        :param title:标题
        :param content:正文
        :param sender:发送人
        :param auth_code: 授权码
        :param receivers:收件人
        :return:
        '''
        # 构建消息
        message = MIMEText(content, 'html', 'utf-8')
        message['From'] = '{}'.format(sender)
        message['To'] = ','.join(receivers)
        message['Subject'] = title

        try:
            smtp_obj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtp_obj.login(sender, auth_code)
            smtp_obj.sendmail(sender,receivers,message.as_string())
            print('发送成功')
        except Exception as e:
            print(e)


    def get_content(self):
        ex=Excel_tools()
        ex.read_work_book(excelpath)
        ex.read_work_sheet('测试用例')
        data=ex.get_all_dic_data()
        datas=''
        for i in range(2,len(data)+2):
            datas+=f'''
                        <tr>   
                            <th>{data[i]['序号']}</th>
                            <th>{data[i]['用例名称']}</th>
                            <th>{data[i]['执行结果']}</th>
                        </tr>
                    '''

        content = f"""
            <html>
                <body>
                    <h3>测试报告</h3>
                    <table border='1'>
                        <tr>   
                            <th>Id</th>
                            <th>scene</th>
                            <th>test_result</th>
                        </tr>
                        {datas}
                    </table>
                </body>
            </html>
            """
        return content


    def send_mail(self,username, passwd, recv, title, content, port=465, file=None):
        '''
        发送邮件函数，默认使用163smtp
        :param username: 邮箱账号 xx@163.com
        :param passwd: 邮箱密码
        :param recv: 邮箱接收人地址，多个账号以逗号隔开
        :param title: 邮件标题
        :param content: 邮件内容
        :param mail_host: 邮箱服务器
        :param port: 端口号
        :return:
        '''
        if file:#如果有附件
            msg = MIMEMultipart()
            # 构建正文
            part_text = MIMEText(content)
            msg.attach(part_text)  # 把正文加到邮件体里面去

            # 构建邮件附件
            part_attach1 = MIMEApplication(open(file, 'rb').read())  # 打开附件
            part_attach1.add_header('Content-Disposition', 'attachment', filename ='测试报告.html')  # 为附件命名
            msg.attach(part_attach1)  # 添加附件
            print('附件邮件发送成功')
        else:
            msg = MIMEText(content,'html', 'utf-8')  # 邮件内容
            print('邮件发送成功')

        msg['Subject'] = title  # 邮件主题
        msg['From'] = username  # 发送者账号
        msg['To'] = ','.join(recv) # 接收者账号列表
        smtp = smtplib.SMTP_SSL(self.mail_host, port=port)
        smtp.login(username, passwd)  # 登录
        smtp.sendmail(username, recv, msg.as_string())
        smtp.quit()



if __name__ == '__main__':
#     from config.VarConfig import auth_code
    # #发送自制测试报告
    # mail = SendMail('smtp.163.com')
    # data=get_content()
    # sender = 'beier0917@163.com'
    # receivers = ['953564459@qq.com']
    # title = '测试报告'
    # content = data
    # auth_code = auth_code
    # mail.send(title, content,sender,auth_code, receivers)
    #print(get_content())

    #发送附件邮件
    mail = SendMail('smtp.163.com')
    send_address = "beier0917@163.com"
    send_password = auth_code
    receive_address = ['953564459@qq.com','2482821110@qq.com']
    title = "测试报告"
    content = "测试报告在附件中"
    attachfilepath = reportpath
    mail.send_mail(send_address, send_password, receive_address, title, content, file=attachfilepath)

