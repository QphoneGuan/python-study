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

#lessom 32-transfer type
str(),int(),float(),bool()

#lesson 33-arithmetic operator
+ - * ** / // %

#lesson 34-assignment operator
= += -+ *= /= %= //= **=

#lesson 35-relational operator
== > < >= <= !=
#在python中可以三元比较，例如30 > 20 > 10结果为True，30 < 40 >35结果也为True（总是让中间和两边的比较）

#leeson 36-logical operator
##逻辑运算符有三种：not,and,or
#1，not后面只要是False和空性的东西，返回的结果都是True,否则返回的就是False
#2，and两边都是布尔值的情况下，只要有一个是False返回的结果都是False。一边布尔值另一边其他类型，则通通返回其他类型的值。
#3，or两边都是布尔值的情况下，只要有一个是True返回的结果都是True。一边布尔值另一边其他类型，若其他类型为空性的东西就当作False执行，否则返回其他类型的值。

#lesson 37-logical operator for non-bool
#1，not后面只要是False和空性的东西，返回的结果都是True,否则返回的就是False ##not '123'返回的结果是False
#2，and两边不管是什么类型，都是先判定左边然后再判定右边，如果左边为False就返回左边的值，否则返回右边的值。（注意是值不是bool值）
a = 0 and 'hello' 
print(a) #返回 0 (注意这里不是返回False)
#3，or两边不管是什么类型，都是先判定左边然后再判定右边，如果左边为True就返回左边的值，否则返回右边的值。（注意是值不是bool值）
a = 0 or 123
print(a) #返回123
a = 123 or 0
print(a) #返回0

#lesson 38-conditional operator
##条件表达式的格式：语句1 if 条件表达式 else 语句2
##比较abc的大小方法
a = 30
b = 32
c = 80
d = a if a > b else b ##方法一
max = d if d > c else c ##方法一
big = (a if a > b else b) if (a if a > b else b) > c else c ##方法二
BIG = a if a > b and a > c else b if b > c else c ##方法三

#lesson 39-priority of operators
#运算符的优先级可以参看python手册，常见的顺序乘除优先于加减，not优先and,and优先or，四则运算优先于逻辑运算。

#lesson 40-if statement(1)
#流程控制语句分为：条件语句和循环语句（按顺序执行和循环执行）
#条件判断语句（if），语法：if 条件表达式 : 语句
if 5 > 3 : print('前者大于后者！')
#如果希望if控制多条语句则通过代码块来执行。后边的语句必须要用缩进。
if True :
  print('热烈欢迎')
  print('关群峰')
  print('指导工作！')
print('欢迎结束')
  
#lesson 41-if statement(2)
    #python是一门严格缩进的语言，在书写代码的时候要么使用tab键，要么使用四个空格键进行缩进
a = input('请输入用户名')
if a == admin:
    print('热烈欢迎管理员')

#lesson 42-'input' function
    #input()函数是用于调取用户输入的数据的
    #input()函数返回值均为字符串类型
    #input()函数返回值可以赋值给变量
    #input()函数也可以用于程序终止的提醒
Num = int(input('please input a number？'))
if Num > 10:
    print('oh my god,your number is above 10')
else:
    print('guess again!')

#lesson 43-if-else statement
if XXX: #（英文的:）
    print('XX') #四个空格缩进
else: #（英文的:）
    print('xx') #四个空格缩进
  
#lesson 44-if-elif-else statement
    #语法：
    if XXX:
        XXX
    elif XXX:
        xxx
    elif XXX:
    ......
    else:    #有时候这个else可以省略
        XXX
    #if-elif-else语句只会执行一个满足条件的代码块。

#lesson 45-task(1)
#score = int(input('请输入小明的期末成绩:'))
#if score == 100 :
#    print('奖励一台BMW')
#elif 80 <= score <= 90 :
#    print('奖励一台iPhone')
#elif 60 <= score <= 79 :
#    print('奖励一本参考书')
#else :
#    print('考的不好！什么奖励都没有')

#lesson 46-task(2)
#stature = float(input('请输入你的身高(cm)：'))
#money = float(input('请输入你拥有的财富(万)：'))
#beauty = float(input('请输入你的颜值（满分600）：'))
#if stature >= 180 and money >= 1000 and beauty >=500 :
#	print('我一定要嫁给他！')
#elif stature >= 180 or money >= 1000 or beauty >=500 :
#    print('嫁吧，比上不足，比下有余！')
#else :
#	print('不嫁！')

#lesson 47-while statement
i = 0 #初始表达式
while i < 8 : #条件表达式
	i += 2 #更新表达式
	print(i,'是8以内的偶数！')
else :
	print('运算结束')
#注意在写while语句的时候不要写成死循环！

#lesson 48-task(1)
n = 100
while n < 1000 :
	if (n // 100) ** 3 + (n // 10 % 10) ** 3 + (n % 10) ** 3 == n :
		print(n)
	n += 1
    
#lesson 49-task(2)
i = 0
result = 0
count = -1
while i <= 100 :
	result += i
	count += 1
	i += 7
print(result)
print(count)

#lesson 50-prime number task
n = int(input('请输入一个整数：'))
i = 2
j = True #创建一个bool变量用于记录是否状态

while i < n :
	if n % i == 0 :
		j = False
	i += 1
if j :
	print(n,'是质数')
else :
	print(n,'不是质数')
#方法二
n = int(input('请输入一个整数：'))
i = 2
j = 0 #引入一个计数参数记录

while i < n :
	if n % i == 0 :
		j += 1
	i += 1

if j > 0 :
	print(n,'不是质数')
else :
	print(n,'是质数')
    
#lesson 51-loop nesting
#*****
#****
#***
#**
#*
#倒三角矩阵举例如下：
i = 5 #外循环初始表达式
while 0 < i <= 5 : #外循环条件表达式
	j = 0 #内循环初始表达式，attention：这个j可以放到外循环起类似作用
	while j < i : #内循环条件表达式
		print(' *',end = '')
		j += 1 #内循环更新表达式
	print()
	i -= 1 #外循环更新表达式

#lesson 52-loop nesting task
#求100以内质数
n = 2
while n <= 100 :
	j = True 
	i = 2
	while i < n :
		if n % i == 0 :
			j = False
		i += 1
	if j :
		print(n)
	n += 1
	
#lesson 53-break and continue
#break 用于立即终止循环
#continue 用于终止一次循环
#pass 用于占位，还没想好这个循环内表达式如何写

#lesson 54/55-prime number optimization task(1-2)
#from time import * #调用time模块
#time() #使用调用的time()函数
#优化（寻找质数）
start = time()
i = 2
while i <2000 :
	j = 2
	k = True
	while j <= i ** 0.5 : #由华谊：因数都是成对出现，所以只要检查根号下的值为止即可！
		if i % j ==0 :
			k = False
			break #加了break，说明一旦出现False就终止循环
		j += 1
	if k :
		print(i)
	i += 1
end = time()
print('程序运行耗费时间为：',end - start,'秒')

#lesson 56-minigame 
print('''请选择你的身份：
							1，唐僧
							2，白骨精''')
choice_1 = input('请选择（1-2）：')
attack = 2
life = 2
if choice_1 == '1' :
	print(f'''你已经选择了唐僧，恭喜你将以唐僧的身份进行游戏！
	你的身份是->唐僧<-，你的攻击力是：  2  你的生命值是：  2
	请选择你要做的操作：
		             1，练级
		             2，打BOSS
		             3，逃跑''')
elif choice_1 == '2' :
	print('2')
else :
	print('3')
choice_2 = input('请选择（1-3）：')

























  







