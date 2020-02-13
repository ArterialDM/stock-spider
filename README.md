# stock-spider

## 前言

### 这是我的python期末考试

## 目录

* [前言](#前言)
* [概述](#概述)
    * [开发环境](#开发环境)
    * [基本原理或技术](#基本原理或技术)
    * [系统需求](#系统需求)
* [程序概要设计](#程序概要设计)
    * [已经实现功能](#已经实现功能)
    * [未实现功能](#未实现功能)
* [程序详细设计](#程序详细设计)
    * [引入库](#引入库)
    * [爬的对象](#爬的对象)
    * [Stock类](#Stock类)
    * [数据库表结构](#数据库表结构)
* [总结](#总结)
* [参考文献](#参考文献)
* [使用截图](#参考文献)

## 概述

### 开发环境

* Windows 10
- Python3
* Pycharm
- MySql8.0

### 基本原理或技术

* 通过新浪股票API获取股票实时信息
- 面向对象设计思想每爬回来一条信息实例化一个Stock类
* 通过Sql查询语言存储爬回来的信息

### 系统需求

* 把所需信息从互联网上爬回来
- 如果必要就需要加入一定的反爬技术
* 用正则表达式处理爬回来的信息
- 爬回来的信息进行数据统计科学计算
* 用多种格式存储爬回来的信息如记事本、Csv、json、xml、 excel

## 程序概要设计

### 已经实现功能

* 通过爬新浪股票API成功获得股票实时信息
- 爬回来的信息用Python字符串处理函数进行信息提取
* 把存储在内存中的信息通过Sql语言写进数据库MySql8.0
- 通过数据库软件MySql进行持久化操作
* 单线程爬股票

### 未实现功能

* 没有加入反爬技术
- 没有使用到正则表达式技术
* 没有把股票信息进行数学统计和科学计算
- 没有把信息存储进如记事本、Csv、json、xml、 excel等多种载体
* 多线程爬股票

## 程序详细设计

### 引入库

    import requests
通过http协议从互联网获取信息。

    import pymysql
用pymysql模块连接数据库软件。

    import time
用time模块设置定时，适当的让爬虫睡睡觉不要拼命地爬。

### 爬的对象

    stockIDs =("sh601008","sh600004","sh601398")
用一个元组存储需要爬的股票的代码，需要爬更多股票的话就修改这个元组。

### Stock类

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
        sql = "INSERT INTO stock(ID,today_open_price,yesterday_close_price,now_price,today_top_price,yesterday_low_price) VALUES ('"+ self.ID+"'"+","+self.today_open_price+","+self.yesterday_close_price+","+self.now_price+","+self.today_top_price+","+self.yesterday_low_price+")"
        try:
            cursor.execute(sql)
            con.commit()
            return True
        except Exception as e:
            print(e)
            con.rollback()
            return False

    …
这是一个专门用来记录每条爬回来的股票信息的类。

### spider()

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

每次到点爬虫该出发了就执行此函数

### 数据库表结构

    create table stock
      (
        count int auto_increment,  
	    ID varchar(20) null,  
	    today_open_price float null,  
        yesterday_close_price float null,  
	    today_top_price float null,
	    yesterday_low_price float null,
	    now_price float null,
	    time timestamp default now() not null,
	    constraint stock_pk
            primary key (count)
      );

每个时间点每支股票爬回来的每条信息对应产生表的一条记录。

## 总结

Python作为一门脚本语言与其他严格的面向对象设计编译型语言相比，编写起来简洁轻松得多,但是事物是具有两面性的，这种简洁快速的编程方式可能会带来不靠谱的计算机软件。

## 参考文献

《Python高级编程》

## 使用截图
