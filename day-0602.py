import requests
import re
import pandas as pd
import pymysql
class huoqu():
    def __init__(self):
        self.num=1
        for i in range(10):
            response = requests.get('http://www.89ip.cn/index_%d.html'%i)
            self.HTML = response.text
            #print(HTML)
            #是一个字符串
            #目标存入mysql
            self.ip = re.compile(r'<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',re.S)
            self.res = re.findall(self.ip,self.HTML)
            self.DButil(self.res)
    def DButil(self,res):
        self.db=pymysql.connect('localhost','root','root','python_an')
        self.cursor = self.db.cursor()
        for ip_ in self.res:
            self.num+=1
            query = """insert into catering_sale (num,IP,port,geographical,perators,final_detection) values (%s,%s,%s,%s,%s,%s)"""
            #print(query)
            values = (self.num,ip_[0].replace('\n', '').replace('\t', ''),ip_[1].replace('\n', '').replace('\t', ''),ip_[2].replace('\n', '').replace('\t', ''),ip_[3].replace('\n', '').replace('\t', ''),ip_[4].replace('\n', '').replace('\t', ''))
            #print(values)
            #print(type(self.num))
            self.cursor.execute(query,values)
        self.cursor.close()
        self.db.commit()
        self.db.close()
if __name__=='__main__':
    huoqu=huoqu()
    huoqu.__init__