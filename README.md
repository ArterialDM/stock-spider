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
    * [User类](#User类)
    * [UserManager类](#UserManager类)
    * [Magazine类](#Magazine类)
    * [MagazineManager类](#MagazineManager类)
* [总结](#总结)
* [参考文献](#参考文献)
* [使用截图](#参考文献)

## 概述

### 开发环境

* Windows10
- python3
* pycharm
- MySql8.0

### 基本原理或技术

* 通过新浪股票API

### 系统需求

* 把

## 程序概要设计

### 已经实现功能

* 订户信息的注册
- 订阅模块
* 管理员可以增加书
- 管理员可以删除库存为0的书
* 杂志信息设定杂志编号、名称、数量、价格这4个变量

### 未实现功能

* 查询功能
- 管理员不能查询库存为0的杂志
* 管理员不能修改杂志数量

## 程序详细设计

### User类

    class User {
      public:
	      int number;
	      char *username;
	      char *password;
	      int money;
	      int magazineList[100];
    …
这是记录每个订阅人的类，每创建一个新订阅人账户，就在堆上new一个User。  
User类的成员变量分别为编号，用户名，密码，钱包余额，已购买的书单。

### UserManager类

    class UserManager {
      public:
	      int userNumber;
	      User * userList[100];
        UserManager()
        bool addUser()
        int isHaveSame(char *newUsername)
        int isHaveAccount(char *thisUsername, char *thisPassword) 
        Bool userAddMagazine(int userNumber,int magazineNumber,MagazineManager *thisMagazineManager) 
        void readMagazine(int userNumber,int magazineNumber) 
        bool addMoney(int userNumber)
        void showUserBuy(int userNumber,MagazineManager thisMagazineManager)
    …
这是一个用来管理订户的类，用来保存订户信息和管理订户的方法。

### Magazine类

    class Magazine {
      public:
        char *title;
	      int number;
	      int price;
	      int quantity;
	      bool flag;
    …
    
这是记录每个订阅人的类，每创建一个新订阅人账户，就在堆上new一个Magazine。  
Magazine类的成员变量分别为书名，书的编号，价格，库存，是否生效。

### MagazineManager类

    class MagazineManager {
      public:
	      Magazine *magazineList[100];
	      int number;
	      MagazineManager() 
	      bool addMagazine() 
	      bool getMagazine(int thisNumber)
	      void showAllMagazine() 
	      void cleanZero() 
	      void search(char key)
    …
    
这是一个用来管理杂志的类，用来储存杂志存放的地址和进行对杂志的各种操作。

## 总结

450多行代码，没什么意义的作业，排版真辛苦，浪费我时间。

## 参考文献

《C++ primer plus》

## 使用截图
