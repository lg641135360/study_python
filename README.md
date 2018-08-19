## python

### 如何变换两个变量

    # 其他语言            python
    temp = x             x,y = y,x 
    x = y 
    y = temp

### python能做什么
![image](https://github.com/lg641135360/study_python/blob/master/jpgs/QQ%E5%9B%BE%E7%89%8720180814075308.png)

### 编程解决生活中的问题

---

### 面向对象
#### 代码组织和构建的方式，让工程更加易于管理，提高代码可读性。

### 一个关于编程的误区
#### web编程只是编程的一个方向

### 什么是代码
#### 现实世界在计算机世界中的映射
### 什么是写代码
#### 将现实世界的事物用计算机语言来描述
---
## python基本数据类型
### Number ：  数字 
####1. 整数 ：int（没有short，int，long之分）
####2. 小数 ：float（没有单精度和双精度之分，实际上为其他语言的双精度）
#### ps：’/‘ 表示除法，’//‘表示整除

### 各进制转换
#### 0b表示2进制
#### 0o表示8进制
#### 0x表示16进制
#### bin(),oct(),hex(),int()分别向2进制，8进制，16进制和10进制转换

### bool：表示真假   
#### ps：True和False要大写，其实就是Number类型的一种1和0
#### 		 空值为False
![image](https://github.com/lg641135360/study_python/blob/master/jpgs/QQ%E5%9B%BE%E7%89%8720180814092039.png)
### complex：复数（非重点）

### str：字符串

    'hello world!'
    
    'let"s go'    // 使用两个单引号或者双引号括住一个引号的句子
    
    '''
    hello
    hello 
    hello
    '''           // 使用3个单双引号定义多行字符串
    # '\nhello\nhello\n' out of IDLE
    
    print("""hello\nhello\nhello\n""")  //使用print函数有换行特性 

	"hello\                             //单双引号换行方式
	world" 

#### 转义字符
##### 特殊的字符，无法"看见"，与语言本身有冲突的的字符
##### \n 换行 \r 回车

    print(r"c:\dev\env")   // 字符串之前加r使其成为原始字符串
#### 字符串的运算

    "hello" + "world"
    # helloworld   out 
    
    "hello" *3
    # hellohellohello out
    
    "hello"[0]
    # h           out
    "hello"[-1]
    # o           out
    "hello"[0:4]
    # hell        // 0--起始下标，4---步长（要取的字符的下标加1，大于整个字符串长度时，取到整个起始到最后）
    "hello"[0:]  
    # hello       out
    "hello"[:5]
    # hello       out

#### 组的概念（list）

    ['123',123,"积分"，True,Flase]    # 可以加入任意的类型
    type([1])   
    # list            out
    [[1,2],[true,"123"],["1","2"]]   # 嵌套列表也称为二维列表

##### 列表的操作

    ["q","w","s","d"][0]  
    # 'q'  out
    ["q","w","s","d"][0:2]
    # ['q','w']  out
    ["q","w","s","d"][-1:]    
    # ['d']                    ps:直接写下标会显示单个字符串，而使用冒号还是显示列表

	["1","2"] * 3
	# ["1","2","1","2","1","2"]  out

#### 元组的概念（tuple）

    (1,2,True,False)   // 跟列表类似
    (1,2,3) + (4,5,6)
    # (1,2,3,4,5,6)  out
    (1,2) * 2
    # (1,2,1,2)  out

	# 一个特别的现象   //ps：list不会有这种现象
	type((1))   // out : int类型
	// 因为这里元组()和运算符号()产生了冲突，所以编译器默认将元组内只有一个元素时类型定义为其元素的类型
	// 而不是元组tuple类型
	# 如何解决？
	(1,)     // 假装不是一个元素即可 
	()       // 定义了一个空元组
### 序列的概念
#### 包括 str list tuple

    // 共有的操作
    'hello world!'[2]   // 序列里面每个元素都会被分配一个序号，有序。
    [1,2,3,4,5][0:]     // 学名：切片

	[1,2,3] */+         // 可以进行数乘运算（*/+）

	3 in [1,2,3]        // 3是否在列表中
	# True
	3 not in [1,2,3]    // 不在列表内  

	len([1,2,3])
	max([1,2,3])
	min([1,2,3])
	max("hello world!")   // 这里会根据ASCI编码来选出最大的字符

	ord("c")              // 输出该字符的ASCI码


###  集合的概念 Set

    type({1,2,3,4})
    # <class 'set'>  out
    {1,2,3}[1]   
    # 报错                 // 集合的特性一：无序
    {1,1,2,2,3,3}
    # {1,2,3}  out        // 集合的特性二：不重复
#### 集合的特殊操作

    {1,2,3,4,5,6} - {4,5}
    # {1,2,3,6}           // 求两个集合的差集
    {1,2,3,4,5,6} & {4,5}
    # {4,5}               // 两个集合的交集
    {1,2,3,4} | {4,6}
    # {1,2,3,4,6}         // 两个集合的并集（去重合并）

	# 定义一个空集合？
	set()
### 字典的概念dict
#### 键值对 实际上还是集合（set）

    # {key1:value1,key2:value2...}
    {"1":"one","2":"two"}["1"]    
    # 'one'                    // 通过key来访问value
    {"1":"one","2":"two","1","three"}
    # {"1":"three","2":"two"}  // 出现相同key时会覆盖原值

	# value取值 任意python基本类型
	# key取值原则 *不可变*  // ps：元组可以，list不行

### 基本数据类型总结
![image](https://github.com/lg641135360/study_python/blob/master/jpgs/QQ%E5%9B%BE%E7%89%8720180817155949.png)

---

## 变量与运算符
### 变量--名字

    A = [1,2,3,4]
    print(A)
    B = [1,2]
    A * 3 + B + A
#### 变量命名规则

    1.首字母不能是数字
    2.首字母可以是字母，_
    3.不能使用系统关键字  // 保留关键字
    4.区分大小写

    a = 1
    b = a
    a = 2
    print(b)
    1

	a = [1,2,3]
	b = a
	a[0] = "1"
	print(b)
	["1",2,3]
	# int str tuple(不可改变) 值类型  list set dict(可变) 引用类型 
	
	# 证明str是不可改变
	a = "hello"
	print(id(a))
	# 444
	a = a + " world"
	print(id(a))
	# 555                   // 从这里看出a换了一个位置，已经不是原来的地址
	"hello"[0] = "l"        // 这里会报错，字符串是不能改变的    

#### 运算符
- 算术运算符
	- //  整除
	- % 求余数
	- ** 乘方  2**2 = 4
- 赋值运算符
	- 落实到赋值（这个很重要）
	- 没有自增自减
- 比较运算符
	- 不止是比较数字
	- 序列都可以
- 逻辑运算符
	- 操作和返回都是bool类型
	- "a" 1 都是bool类型都是True
	- int float 为0都是False
	- 空字符串为False
	- 空列表为False
	

    1 and 0
    # 0
    1 and 2
    # 2                             // 要判断改式子是否为真需要看到第二个，又因为第二个为真，直接返回第二个
    1 or 2
    # 1                           // 只需要第一个就判断为真，则返回1
	   - 成员运算符
		   - 判断一个元素是否在另外一组元素内
		   - 返回值为bool值
		   - 特别的，字典使用是检测的是key
	   - 身份运算符
		- == 比较的是两个变量的值，is比较的两个变量的身份（内存地址）是否相等
		- 变量的三个特征 id type value
		- 判断类型 isinstance(a,int) or isinstance(a,(int, float))

####- 位运算符
![image](https://github.com/lg641135360/study_python/blob/master/jpgs/QQ%E5%9B%BE%E7%89%8720180817191925.png)


### 表达式
#### 表达式（Expression）是由操作符（Operator）和操作数（Operand）所构成的序列
##### 表达式的优先级

    not a or b + 2 == c
    # false                     // 没有 = 赋值时候基本上是从左到右运算2
    // not > and > or
    # ((not a) or ((b + 2) == c)

### 使用ide编程
#### vscode
![image](https://github.com/lg641135360/study_python/blob/master/jpgs/QQ%E5%9B%BE%E7%89%8720180818214123.png)
#### ide的优点
##### 智能感知，断点调试
##### 推荐插件
![image](https://github.com/lg641135360/study_python/blob/master/jpgs/Snipaste_2018-08-18_21-55-24.png)

#### vs语法规则以及一些vscode小技巧

    ctrl + `    --- 调出控制台
    tab         --- 自动补全文件名


	# 流程控制语句
    #           --- 单行注释
    '''
	    code
	'''         --- 多行注释

	# tip
	ctrl + /    --- vscode中单行注释
	alt + shift + a    --- 选中多行注释

	# constant  --- 形式上的常量
	account = "1"   // python中没有严格意义上的常量
	ACCOUNT = "1"   // 代码规范是要将形式上的常量全部用大写代替
	
	# vscode中使用bash作为默认终端
	// 在用户设置中添加如下代码
	// 配置git-bash为默认终端
    "terminal.integrated.shell.windows": "C:\\dev\\env\\Git\\bin\\bash.exe"

    # snippet 片段

    # if code:
    #     pass
    # else:
    #     pass

    a = True

    if a:
        print("hello")
    else:
        print("bye bye")
    
    // 进入snippet 代码片段内可以直接按tap编写if条件，if内

    # pass 空语句/占位符

