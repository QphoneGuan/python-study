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
#唐僧大战白骨精#
print('-'*20,'欢迎光临唐僧大战白骨精','-'*20)

print('''请选择你的身份：
			            1，唐僧
					    2，白骨精''')
choice = input('请选择（1-2）：')

player_attack = 2
player_life = 2
boss_life = 10
boss_attack = 10
print(67*'-')

if choice == '1' :
	print(f'''你已经选择了唐僧，恭喜你将以唐僧的身份进行游戏！

你的身份是->唐僧<-，你的攻击力是：  {player_attack}  你的生命值是：  {player_life}''')

elif choice == '2' :
	print(f'''什么你竟然选择了白骨精？太不要脸了，系统将自动分配你以唐僧的身份进行游戏

你的身份是->唐僧<-，你的攻击力是：  {player_attack}  你的生命值是：  {player_life}''')

else :
	print(f'''你输入的选项有误，系统将自动分配你以唐僧的身份进行游戏

你的身份是->唐僧<-，你的攻击力是：  {player_attack}  你的生命值是：  {player_life}''')

print(67*'-')

while True :
	operation = input('''
请选择你要做的操作（1-3）：
		         1，练级
		         2，打BOSS
		         3，逃跑
请选择（1-3）：''')
	print(67*'-')
	if operation == '1' :
		player_attack += 2
		player_life += 2 
		print(f'''
=======================================

恭喜你！->唐僧<-，你升级了，你现在的攻击力是：  {player_attack}  你的生命值是：  {player_life}

=======================================''')
	elif operation == '2' :
		boss_life -= player_attack
		print('唐僧攻击了白骨精')
		print(f'白骨精受到了{player_attack}点伤害')
		print(67*'-')

		if boss_life <= 0 :
			print('恭喜唐僧战胜了白骨精，游戏结束')
			print(67*'-')
			break

		player_life -= boss_attack	
		print('白骨精向唐僧发起了反击！')
		print(f'唐僧受到了{player_attack}点伤害！')
		print(67*'-')

		if player_life <= 0 :
			print('唐僧阵亡，游戏结束！')
			print(67*'-')
			break	
	elif operation == '3' :
		print('只见那唐僧一溜烟跑了，游戏结束！')
		print(67*'-')
		break
	else :
		print('您的输入有误，请重新输入！')
		print(67*'-')

#lesson 57-list
##列表是python中的一个对象，和字符串，数字，bool，None一样
##列表中可以有顺序的存放对象的对象
##语法：my_list = []
my_list = ['hello',123,None,True,[3,4,5],if]
##获取列表中的元素需要利用索引
##索引是表示列表中元素顺序的一个整数，即第一个元素的索引是0，以此类推。
##注意：索引也可以为负数，-1表示倒数第一个元素,以此类推。
print(my_list[1]) #结果为123
print(my_list[-2]) #结果为[3,4,5]
##获取列表中元素的个数的方法是len()函数
print(len(my_list)) #结果为6
##列表中元素的个数为：最大索引+1

#lesson 58-list slice
##切片是指从列表中获取一个子列表,而且不改变原来的列表。
##语法：列表[起始:终止:步长]，步长默认为1，可以省略。包括起始位置的元素，但是不包括终止位置的元素！
your_list = ['秦始皇','康熙','雍正','刘邦','曹操','刘备','孙权','朱元璋','赵匡胤']
slice_1 = your_list[0:3]
slice_2 = your_list[::2]
slice_3 = your_list[:6:3]
slice_4 = your_list[::-2]
slice_5 = your_list[-1:1:-2] #注意这个是指先切取倒数第一个位置的元素和第一个元素之间的元素（不包括第一个），然后按照步长2，反向取元素。
print(slice_5) #结果为：['赵匡胤', '孙权', '曹操', '雍正']

#lesson 59-list operation
##合并列表。list_A + list_B，两个列表内元素合并为一个列表
##复制列表。数字*list_A，列表内元素重复多次
##判断元素是否在列表中
your_list = ['秦始皇','康熙','雍正','刘邦','曹操','刘备','孙权','朱元璋','赵匡胤']
print('曹操' in your_list) #结果为真
print('李世民' not in your_list) #结果为真
##列表元素个数：
print(len(your_list)) #结果为9
##元素中最大值和最小值(数字和字符串均可)
print(max(your_list),min(your_list)) #结果为：雍正 刘备
##对列表进行索引和计数的方法： (方法method类似于函数，但是必须通过对象.方法的形式调用)
###查找某个元素在索引中的位置：list.index(x,y,z) ,x 为待查元素（不存在会报错），y为从哪儿开始找，Z为在哪儿查找结束
new_list = ['秦始皇','康熙','雍正','秦始皇','曹操','刘备','孙权','秦始皇','赵匡胤']
print(new_list.index('秦始皇',4,9)) #结果为7
###某元素在列表中出现的次数：list.count()
print(new_list.count('秦始皇')) #结果为：3

#lesson 60-sequence
#序列是python中最基本的数据结构（是指计算机中的存储顺序）
#用于保存一组有序的数据，所有的数据在序列中有唯一的位置（索引）
#序列分为：可变序列（例如列表list）和不可变序列(例如字符串str，元组tuple)

#lesson 61- modify list
#通过索引的方式修改列表中的元素
my_list = ['张三','李四','王二','麻子','周五','郑王']
my_list[0] = '赵六' #将张三替换为赵六
#通过del 删除列表中的元素
del my_list[3] #删除列表中的第四个元素
#通过切片来修改列表
my_list[0:2] = ['钱七','朱八'] #将第1和2个元素替换为钱七和朱八
my_list[1:5:2] = ['关九','陆一'] #将李四和麻子替换为关九和陆一，一旦设置步长就必须替换元素个数一致，没有设置步长可以个数不一样
my_list[0:2] = ['孙悟空','猪八戒','沙和尚'] #将张三和李四替换为孙悟空，猪八戒，沙和尚
#通过切片来插入列表中的元素
my_list[0:0] = ['吴六'] #在索引为0的位置插入元素 吴六
my_list[1:1] = ['1','2','3'] #在索引为1的位置插入元素 1 2 3
#通过切片来删除元素
del my_list[::2] #删除元素张三，王二，周五
#attention:利用切片和索引来进行修改时，只对序列起作用（字符串，列表等等），如果要想修改，通过list()函数转换，当然能够被list()的对象也必须是序列。

#lesson 62-methods of list
my_list = ['刺客','法师','飞侠','战士','道士']
##添加元素
my_list.append('骑士') #在列表末尾追加一个元素(必须是一个)
my_list.insert(2,'巫师') #在指定的索引位置添加一个元素(必须是一个)
my_list.extend(['角斗士','侠客','忍者']) #在列表末尾追加一个序列(可多个元素)
##删除元素
my_list.clear() #清除列表中的所有元素
my_list.remove('道士') #删除列表中指定的一个元素（必须是一个），如果列表有多个同样的元素，那就默认删除第一个
my_list.pop(1) #删除列表中指定索引的一个元素并返回被删除元素(不传参数默认删除最后一个元素)
print(my_list.pop(1)) #返回值：法师
##反转列表
my_list.reverse() #将列表中元素反转
##排序列表
my_list.sort() #将列表中元素按照升序排列，参数可以为reverse = True
my_list.sort(reverse = True) #将列表中元素按照降序排列

#lesson 63-iteration of list
#遍历是指将列表中的所有元素一一取出来
#通过while循环遍历
my_list = ['刺客','法师','飞侠','战士','道士']
i = 0
while i < len(my_list) :
    print(my_list[i])
    i += 1
#通过for循环遍历
##语法：
##for x in x_list :
##    print(x)
my_list = ['刺客','法师','飞侠','战士','道士']
for x in my_list :
	print(x)
	
#lesson 64-66 -miniprogram EMS

print('='*20,'欢迎使用员工管理系统','='*20)

emps = ['\t孙悟空\t18\t男\t花果山']

while True :
	print('')
	print('请选择你要做的操作：')
	print('\t1，查询员工；')
	print('\t2，添加员工；')
	print('\t3，删除员工；')
	print('\t4，退出系统；')
	print('-'*54)
	choose = input('请选择（1-4）：')
	if choose == '1' :
		print('\t序号\t姓名\t年龄\t性别\t住址')
		num = 1
		for x in emps :
			print(f'\t{num}{x}')
			num += 1
	elif choose == '2' :
		name = input('请输入员工的姓名：')
		age = input('请输入员工的年龄：')
		gender = input('请输入员工的性别：')
		address = input('请输入员工的住址：')
		new_emp = f'\t{name}\t{age}\t{gender}\t{address}'

		print('添加的员工信息如下：')
		print('-'*54)
		print('\t姓名\t年龄\t性别\t住址')
		print(f'{new_emp}')
		print('-'*54)
		confirm = input('是否确认[Y/N]：')
		if confirm == 'Y' or confirm == 'y' :  #这是个坑，之前我写成了confirm = 'Y' or 'y'
			emps.append(new_emp)
			print('添加成功！')
		else :
			print('添加失败！')
	elif choose == '3' :
		del_n = int(input('请输入所要删除员工的编号：'))
		if 0 < del_n <= num :
			del_i = del_n - 1
			print('以下员工信息将被删除！')
			print('\t序号\t姓名\t年龄\t性别\t住址')
			print(f'{del_n}{emps[del_i]}') #这是个坑，刚开始写的时候没有将序号和内容分别赋值，导致删除员工之后序号没自动变化
			confirm_1 = input('是否确认[Y/N]：')
			if confirm_1 == 'Y' or confirm_1 == 'y' : 
				emps.pop(del_i)
				print('删除成功！')
			else :
				print('删除失败！')
		else :
			print('您的输入有误，请重新操作！')

	elif choose == '4' :
		print('系统已退出，欢迎下次使用！')
		break
	else :
		print('您的输入有误，请重新输入！')
		
#lesson 67-range
#range()函数是生成一个自然数组成的序列
#语法：range(起,止,步长)，表示从起始自然数开始，到终止的自然数为止（不包括终止自然数），这个序列需要使用list()函数返回值
print(list(range(3))) #结果为[0,1,2] 默认起为0，步长为1
print(list(range(2,8,2))) #结果为[2,4,6]
print(list(range(8,2,-2))) #结果为[8,6,4]
print(list(range(1,4,-1))) #结果为[]
#for循环经常和range函数一个使用。
for i in range(1,4,2) :
	print(i)
#for循环和while循环一样，可以和else，break，continue一起使用

#lesson 68-tuple
#元组是一个不可变序列。
#语法：
my_tuple = ('hello','3','4',45)
my_tuple_1 = 'hello','3','4',45
my_tuple_2 = ()
my_tuple_3 = 'hello',
my_tuple_4 = ('hello',)
#以上都是创建元组的方法，注意创建一个元素的元组要加,号
#对列表所作的所有不改变列表的操作，对元组一样适用
my_tuple[i]
my_tuple[2:4]
len()
in
not in
max() 
min()
my_tuple.count(x)
my_tuple.index(x,a,b)
#对序列（字符串，元组，列表）进行解包
my_tuple = (1,2,3,'hello')
a,b,c,d = my_tuple
print('a=',a) #结果为：1
print('b=',b) #结果为：2
print('c=',c) #结果为：3
print('d=',d) #结果为：hello
e,*f,g = 'hello','world','mydear',1,2,3 #同理，e和g前面也可以加*，但是所有变量只能加一个*
print('e=',e) #结果为：e = hello
print('f=',f) #结果为：f = ['world','mydear',1,2] 
#解包就是将元组中的元素赋值给多个变量，当变量少于元组元素个数时可加*解包，加星的变量被赋值为剩余元素组成一个列表
print('g=',g) #结果为：g = 3
a,b = b,a #将元素a和元素b对调

#lesson 69-variable object
#在python中，每个对象有三个标签，id，class和value
#可变对象是指对象中的value可以改变，例如列表就是可变对象
#改对象
a = [1,2,3,4]
b = a
b[0] = 10
print(a) #结果为[10,2,3,4] id不变
print(b) #结果为[10,2,3,4] id不变
#改变量
e = [1,2,3,4]
f = e
f = [2,3,4,5]
print(e) #结果为[1,2,3,4] id改变
print(f) #结果为[2,3,4,5] id改变

#lesson 70- ==和is
#==和!=是用来比较2个对象的value是否一致
#is和is not 用来比较2个对象的id是否一致
a = [1,2,3]
b = [1,2,3]
print(id(a)) #结果为2733454509256
print(id(b)) #结果为2733454509192
print(a == b) #结果为True
print(a is b) #结果为False

e = [1,2,3]
f = e
print(id(e))
print(id(f))
print(e == f) #结果为True
print(e is f) #结果为True

g = [1,2,3]
g = h
g[0] = 10
print(id(g))
print(id(h))
print(g == h) #结果为True
print(g is h) #结果为True
#一般来说通过=赋值的都是不同对象。
























  







