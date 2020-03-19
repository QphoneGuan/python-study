# python-study

#lesson 24-string
#about string
a = "子曰:"学而时习之，不亦说乎！"" #error，嵌套错误，不能用同样的EN双引号
b = '''白日依山尽
黄河入海流
欲穷千里目
更上一层楼''' #换行且保留多行格式
c = '国破山河在，\
城春草木深。\
感时花溅泪，\
恨别鸟惊心' #写法换行不保留多行格式
d = '慈母手中线，\n游子身上衣，\n木桶为寄主，\n为文物叹息！' #换行为多行格式
#\表示输入换行，\\表示斜杠，\n表示格式换行，\t表示插入一个制表符，\uXXXX表示插入一个utf-8码

#lesson 25-the format string
a = 'a = '+'123' 
print(a)
print('a = ','123') #逗号多一个空格
#字符串4种占位符：%s 字符串,  %f 浮点数,  %d 整数,  f'abc{X}{Y}def'
#扩展用法：%3.5s,%.2f,%2.4d
b = '热烈欢迎%3.4s莅临指导%8.9s公司！'%('JerryQuan','Amazon')
print(b) #输出的结果是：热烈欢迎Jerr莅临指导  Amazon公司
c = "本月的营业额是%.1f元人民币，比上个月上涨了%s%d"%(13400.21,'%',25.2) #注意数字不用引号
print(c) #输出的结果是：本月的营业额是13400.2元人民币，比上个月上涨了%25
d = f'热烈欢迎{a}{b}莅临指导' #输出的结果就是把定义过的a和b带入这个字符串

#lesson 26-copy string
a = 'welcome to China！ '
b = a * 3 #print(b) 输出welcome to China! welcome to China! welcome to China! 

#lesson 27-bool and None
#布尔值只有两种：True真，False假，两者都是int型，True表示1，False表示0.可以进行计算。
#空值只有一种：None
#Attention:True,False and None一定要区分大小写，否则会报错！

#lesson 28-check type
#type()函数用来返回字符类型，返回值需要print()出来方可显示
print(type("hello")) #<class 'str'>
print(type(123)) #<class 'int'>
print(type(123.32)) #<class 'float'>
print(type(False)) #<class 'bool'>
print(type(None)) #<class 'NoneType'>

#lesson 29-objective
#Python是一种面向对象的语言，CPU通过调取内存中的数据进行计算，而这些数据就是放在内存中的某些区域的。
#这些数据就是对象。

#lesson 30-structure of objective
#对象的数据结构包括三个部分：
  1##id（标识），指数据的编号，在Cpython中是数据在内存中的地址，一经创建不可改变！
  id()#函数返回标识值 #print(id('hello'))打印的是一串地址数据
  2##type（类型），指数据的具体类型，例如str,float,bool,None,int等等，一经创建不可改变！
  type()#函数返回类型#print(type(True))打印结果为：<class 'bool'>
  3##value（值），指数据的具体内容，例如：123，"hello",True等等，一般不可改变，存在特例，以后再说。

#lesson 31-variable and objective

  







