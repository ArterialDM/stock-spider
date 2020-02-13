import requests
import pymysql
import time

class Stock:
    def __init__(self, ID, today_open_price,yesterday_close_price,now_price,today_top_price,yesterday_low_price):
        self.ID=ID.split('_')[2]
        self.today_open_price=today_open_price
        self.yesterday_close_price=yesterday_close_price
        self.now_price=now_price
        self.today_top_price=today_top_price
        self.yesterday_low_price=yesterday_low_price

    def toString(self):
        print("股票代码:",self.ID)
        print("今日开盘价:", self.today_open_price)
        print("昨日收盘价:", self.yesterday_close_price)
        print("当前价格:", self.now_price)
        print("今日最高价:", self.today_top_price)
        print("今日最低价:", self.yesterday_low_price)

    def store(self):
        sql = "INSERT INTO stock(ID,today_open_price,yesterday_close_price,now_price,today_top_price,yesterday_low_price) VALUES ('"   +   self.ID  + "'" +  ","+self.today_open_price+","+self.yesterday_close_price+","+self.now_price+","+self.today_top_price+","+self.yesterday_low_price+")"
        try:
            cursor.execute(sql)
            con.commit()
            return True
        except Exception as e:
            print(e)
            con.rollback()
            return False

stockIDs =["sh601008","sh600004","sh601398"]

def spider():
    for stockID in stockIDs:
        url = 'http://hq.sinajs.cn/list=' + stockID
        response = requests.get(url)
        msg = response.text
        msg_unit = msg.split(',')
        stock = Stock(msg_unit[0], msg_unit[1], msg_unit[2], msg_unit[3], msg_unit[4], msg_unit[5])
        stock.toString()
        if(stock.store()):
            print("成功写入数据库")
        else:
            print("写入数据库失败")


i=1
while(True):
    print("爬虫出发",i)
    i=i+1
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1999113WDM', db='stock')
    cursor = con.cursor()
    spider()
    con.close()
    print("爬虫睡觉10s")
    time.sleep(10)
