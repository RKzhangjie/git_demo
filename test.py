#猜数字
# import random
# num=random.randint(1,100)
# flag = True
# count=0
# while flag:
#     num1 = int(input("输入你猜的数字："))
#     count+=1
#     if num1 == num:
#         print("猜对了")
#         flag=False
#     elif num1 <num:
#         print("小了")
#     else:
#         print("大了")
# print(f"你一个猜了{count}次")

#99乘法表
# i=1
# while i<=9:
#     j = 1
#     while j<=i:
#         print(f"{j}*{i}\t",end="")
#         j+=1
#     i+=1
#     print()

#for循环判断有几个a
# name = "itheima is a brand of itcast"
# count=0
# for x in name:
#     if x == "a":
#         count+=1
# print(f"一共有{count}个a")
# for x in range(10):
#     print(x)
# for x in range(5,10):
#     print(x)
# for x in range(5,10,2):
#     print(x)
# for x in range(10):
#     print("送玫瑰花")
# oushu=0
# for x in range(1,100):
#     if x % 2 == 0:
#         oushu+=1
# print(oushu)
#for循环嵌套实例
# for i in range(1,101):
#     print(f"这是向小美表白的第{i}天")
#     for j in range(1,11):
#         print(f"者是向小美送的第{j}朵花")
#     print(f"第{i}天结束")
#
# print(f"第{i}天表白成功")

#break continue 发工资实例
# money = 10000
# for x in range(1,21):
#     import random
#     num = random.randint(1,10)
#     if num<5:
#         print(f"员工{x}绩效小于5，无法领取工资。")
#         continue
#     if money >=1000:
#         money -=1000
#         print(f"员工{x}，满足条件可以发工资1000")
#     else:
#         print(f"公司余额{money}，无法继续发工资请下个月再来。")
#         break

# def shuchu():
#     print("函数测试！")
# shuchu()

# def add(x,y):
#     result = x+y
#     return  result
# x=add(5,10)
# print(x)

# num =100
#
# def testA():
#     print(num)
#
# def testB():
#     global num
#     num=500
#     print(num)
#
# testA()
# testB()
# print(num)

# #函数ATM实例
# #定义全局变量 余额和用户名
# money = 5000000
# name = None
# #请求用户输入名字
# name = input("请输入您的姓名：")
# #定义调查函数
# def query(show_header):
#     if show_header:
#         print("----------查询余额----------")
#     print(f"{name}您好，您的余额剩余{money}元")
# #定义存款函数
# def saying(num):
#     global money#在函数内部定义全局变量
#     money += num
#     print("----------存款-------------")
#     print(f"{name}，您好，存款{num}元成功！")
#     #调用查询函数
#     query(False)#为否则不输出if的代码
# #定义取款函数
# def get_money(num):
#     global money
#     money -= num
#     print("----------取款-------------")
#     print(f"{name},您好，取款{num}元成功！")
#     #调用查询函数
#     query(False)
# #定义主菜单函数
# def main():
#     print("-----------主菜单-----------")
#     print(f"{name}您好，欢迎来到银行ATM，请选择操作：")
#     print("查询余额\t[请输入1]")
#     print("存款\t\t[请输入2]")#通过\t来对齐输出
#     print("取款\t\t[请输入3]")
#     print("退出\t\t[请输入4]")
#     return input("请输入您的选择：")
# #设置无限循环，确保程序不退出
# while True:
#     keyboard_input =main()
#     if keyboard_input == "1":
#         query(True)
#         continue#通过continue继续下一次循环，一进来就退回到主菜单
#     elif keyboard_input == "2":
#         num=int(input("您想要存多少钱?请输入:"))
#         saying(num)
#         continue
#     elif keyboard_input == "3":
#         num =int(input("请输入您要取多少钱："))
#         get_money(num)
#         continue
#     else:
#         print("程序退出")
#         break#通过break退出循环

#列表
#
#元组
# yuanzu1 = (1,"元组","元组")
# print(yuanzu1,type(yuanzu1))
# yuanzu2 = (1,)#必须有,
# print(f"{yuanzu2}{type(yuanzu2)}")
# yuanzu3=tuple()
# print(yuanzu3)
# index = yuanzu1.index("元组")
# print(index)
# count = yuanzu1.count("元组")
# print(count)
# len=len(yuanzu1)
# print(len)
#字符串
# str1 = "字符串1 字符串2 字符串3 字符串1"
# print(str1[2])
# #字符串替换
# str2=str1.replace("字符串2","字符串4")
# print(str2)
# print(str1)
# #字符串分割
# str3 = str1.split(" ")
# print(str3)#分割成list
#序列切片
# my_list = [0,1,2,3,4,5,6]
# result1 = my_list[1:4]#取1-4不不包含4，没写步长就默认为1. 结果为[1, 2, 3]
# print(result1)
#
# my_tuple = (0,1,2,3,4,5,6)
# result2 = my_tuple[:]#只写:起始和截至都不写代表从头到尾，步长为1。结果为(0, 1, 2, 3, 4, 5, 6)
# print(result2)
#
# my_str = "01234567"
# result3 = my_str[::2]#步长为2，全取。结果为：0246
# print(result3)
#
# my_list = [0,1,2,3,4,5,6]
# result4 = my_list[::-2]#将序列反过来，全取。结果为：[6, 4, 2, 0]
# print(result4)
#
# my_list = [0,1,2,3,4,5,6]
# result5 = my_list[::-1][1:5]#将序列倒过来，再进行切片取出。结果为：[5, 4, 3, 2]
# print(result5)
#
# my_str = "这是测试的第一句,这是测试的第二句,这是测试的第三句"
# result6 = my_str.split(",")[1].replace("测试","")[::-1]#以","分割成list,选择1(第二个list),将其中的"测试"替换成空，再反序列以步长为1全取。
# print(result6)
#
# #将list的元素通过for循环存入集合
# my_set = set()
# my_list = [1,2,3,4,5,6]
# for x in my_list:
#     my_set.add(x)
# print(my_set)

#字典
# my_dict = {"字典1":57,"字典2":"2",3:"字典3"}
# print(my_dict["字典1"])
# print(my_dict["字典2"])
# print(my_dict[3])
# my_dict ["字典4"] = 4
# print(my_dict)
# my_dict [3] = "3"
# print(my_dict)
# keys = my_dict.keys()
# print(keys)

#返回多个返回值
# def test_result():
#     return 1,2
# x,y=test_result()
# print(x)
# print(y)

# my_list = [1,2,3]
# my_tuple = (1,2,3)
# my_str = "123"
# my_set = {1,2,3}
# my_dic = {1:"第一个","第二个":2,"第三个":3}
#
# print(str(my_dic))

# my_list = [1,2,3]
# my_tuple = (1,2,3)
# my_str = "123"
# my_set = {1,2,3}
# my_dic = {1:"第一个","第二个":2,"第三个":3}
# print(sorted(my_set,reverse=True))

# def test_func(computer):
#     result = computer(1,2)
#     print(result)
#
# # def computer(x,y):
# #     return x+y
#
# test_func(lambda x,y:x+y)

# f=open("F:\word.txt","a",encoding="UTF-8")
# f.write("追加内容")
# f.flush()

# try:
#     print(name)
# except:
#     print(n)

# from time import *
# print("开始")
# sleep(3)
# print("结束")

# import json
# d = {"字典1":1,"字典2":2,"字典3":3}
# s = json.dumps(d,ensure_ascii=False)
# print(s)
# print(type((s)))
#
# n = '{"字典1": 1, "字典2": 2, "字典3": 3}'
# str_jon = json.loads(s)
# print(n)
# print(type(n))

#折线图
#from pyecharts.charts import Line
# line = Line()
# line.add_xaxis(["中国","美国","英国"])
# line.add_yaxis("GDP",[30,20,10])
# line.render()

#地图
# from pyecharts.charts import Map
# map = Map()
# data = [
#     ("北京",499),
#     ("上海",399),
#     ("湖南", 299),
#     ("台湾", 199),
#     ("广东", 99)
# ]
#
# map.add("疫情地图",data,"china")
#
# map.render()

#柱状图
# from pyecharts.charts import Bar, Timeline
#
# bar = Bar()
#
# bar.add_xaxis(["中国","美国","英国"])
# bar.add_yaxis("GDP",[30,20,10])
# bar.reversal_axis()#反转X,Y
#
# bar.render()

#创建对象
#先创建类
# class Student:
#     name = None
#     age = None
#     gender = None
#     native_place = None
# #创建对象
# stu1 = Student()
# #给对象属性赋值
# stu1.name="张三"
# stu1.age=20
# stu1.gender = "男"
# stu1.native_place = "四川省"
# #输出
# print(stu1.name)
# print(stu1.age)
# print(stu1.gender)
# print(stu1.native_place)

# class Student:
#      name = None
#      def say_hi(self):
#          print(f"hello！我是{self.name}")
# stu =Student()
# stu.name="张三"
# stu.say_hi()

#构造方法
# class Student:
#     def __init__(self,name,age,tel):
#         self.name =name
#         self.age = age
#         self.tel = tel
#         print("Student类创建了一个类对象")
# student = Student("张三",22,153866666)
# print(student.name)
# print(student.age)
# print(student.tel)

# class Student:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#         list = [name,age,address]
#         print(list)
#
# stu_dict = {}
# for x in range(10):
#     print(f"当前录入第{x+1}位学生信息,共需要录入10位学生信息")
#     name = input("请输入学生姓名:")
#     age = input("请输入学生年龄：")
#     address = input("请输入学生地址:")
#     stu = Student(name,age,address)
#     stu_dict[f"学生{x+1}"] = {}
#
# print(f"录入完毕结果为:{}")

#P114 学生信息录入交作业
# 练习：学生信息录入
# 构造类Student
# class Student:
#     def __init__(self, name, age, add):
#         self.name = name
#         self.age = age
#         self.add = add


# 创建空字典，存放学生信息
# stu_dict = {}
#
# # for循环录入信息
# for i in range(2):
#     print(f"当前录入第{i + 1}位学生信息，总共需要录入10位学生信息。")
#     stu = Student(input("请输入学生姓名："),
#                   input("请输入学生年龄："),
#                   input("请输入学生地址：")
#                   )
#     stu_dict[f"学生{i+1}"] = {}
#     stu_dict[f"学生{i+1}"]["姓名"] = stu.name
#     stu_dict[f"学生{i+1}"]["年龄"] = stu.age
#     stu_dict[f"学生{i+1}"]["地址"] = stu.add
#
#     print(f"学生{i + 1}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.add}】")
#
# print("所有学生信息录入完毕。")
#
# print(stu_dict)

#封装实例
# class Phone:
#     __is_5g_enable = False #私有成员变量 5G状态
#
#     def __check_5g(self):#私有成员方法
#         if self.__is_5g_enable:
#             print("5G开启")
#         else:
#             print("5G关闭")
#
#     def call_by_5g(self):#公有成员方法  因为对象不能调用私有成员，所以构造了一个公有成员方法
#         self.__check_5g()
#         print("正在通话中")
# phone = Phone()
# phone.call_by_5g()

#继承实例
# class father:
#     name = "父亲"
#     age = 40
#
# class son(father):
#     name = "儿子"
#     def result(self):
#         print(super().name)
# n= son()
# n.result()

#
# inf:son = son()
# stu:str ="name"
# my_list : list = [1,2,3,4]
# my_dict = {"字典1":1,"字典2":2} #type:dict[str,int]

#多态
# class Animal:
#     def speak(self):
#         pass
# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵")
# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")
#
# def make_speak(animal:Animal):
#     animal.speak()
#
# cat = Cat()
# dog = Dog()
#
# # dog.speak()
# # cat.speak()
# make_speak(cat)
# make_speak(dog)

# from pymysql import Connection
# #获取到MYSQL数据库的链接对象
# conn = Connection(
#     host="localhost",#主机名
#     port =3306,     #端口
#     user="root",    #用户名
#     password="123456"#密码
# )
#
# print(conn.get_server_info())#输出MYSQL版本号
# #获取游标对象
# cursor = conn.cursor()
# conn.select_db("test") #优先选择数据库 USE数据库
# #使用游标对象，执行sql语句
# cursor.execute("CREATE TABLE test_pymsql(id INT ,info VARCHAR(225))")
# #关闭数据库的链接
# conn.close()