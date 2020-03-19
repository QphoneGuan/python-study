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







