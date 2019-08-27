import smtplib                                                            #用于发送邮件和连接发送邮件服务器
from email.mime.text import MIMEText                                      #发送邮件的格式（组织邮件）
import time
class Send_Email(object):
    global sendUser
    global mailhost
    global password
    password = 'baobao905175'
    mailhost = 'smtp.163.com'
    sendUser = '15901764039@163.com'
    def send_mail(self,user_list,sub,content):                            #发送邮件需要的收件人user_list，主题sub，内容content
        User = '迟荣宝'+'<'+sendUser+'>'                                    #发送邮件的人
        message = MIMEText(content,_subtype='plain',_charset='utf-8')       #发送邮件的内容，格式，编码
        message['Subject'] = sub                                            #发送邮件的主题
        message['From'] = User                                              #邮件的发送者
        message['To'] = ';'.join(user_list)                                 #发送给谁
        smtpServer = smtplib.SMTP()                                         #构建一个邮件服务器，用163可以不用写host,port
        smtpServer.connect(mailhost)                                        #用这个服务区连接163
        smtpServer.login(sendUser,password)                                 #登录163邮箱服务器
        smtpServer.sendmail(User,user_list,message.as_string())             #发邮件谁发，发给谁，内容
        smtpServer.close()

    def send_main(self,success_list,fail_list):
        now = time.strftime('%Y-%m-%d %H_%M_%S')
        # user_list = ['18019237119@163.com']   #发送给多人，姚写多个user_list
        user_list = ['1298862728@qq.com']
        sub = '接口自动化测试报告'
        success_num = len(success_list)
        # print(success_num)
        fail_num = len(fail_list)
        # print(success_num)
        total_num = success_num + fail_num
        success_num_rate = '%.2f%%'%(success_num/total_num*100)
        fail_num_rate = '%.2f%%'%(fail_num/total_num*100)
        content = '%s   本次接口自动化测试一共运行的测试用例为%s个，通过个数为%s个，失败个数为%s个，通过率为%s，失败率为%s'%(now,total_num,success_num,fail_num,success_num_rate,fail_num_rate)
        self.send_mail(user_list,sub,content)

if __name__ == '__main__':
    aa = Send_Email()
    aa.send_main([1,2,3],[4,5])