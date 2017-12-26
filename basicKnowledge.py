1,IO：计算机输入时input，输出是output，因此我们把输入输出称为input/output，简写IO。python的IO是input/print.
2,计算机类型
	整形
	浮点型
	字符串：单引号双引号需要用\转义eg：str='I\'m ok';
		特殊 \n 换行 \t 制表符 \自身转义
		r''内的字符串默认不转义
		''''...'''提示符 换行
	布尔值
	空值：None
3，变量：变量名必须是大小写英文、数字、和_的组合，且不能用数字开头
4，常量：通常用大写的变量名来表示常量
5，字符编码：ord('a')获取字符整数表示；chr(65)把编码转换成对应的字符
		Python的字符串类型时str，在内存中以Unicode表示，一个字符对应若干字节，如果在网络上传输，或者保存子磁盘上，就需要把str变为以字节为单位的bytes
		'A'.encode('utf-8') 对str类型转换成bytes类型
		b'A'.decode('utf-8')把bytes类型转换成str类型
		str类型：字符为单位；bytes类型：字节为单位
		注释：#!/usr/bin/env python3 这是一个python可执行程序
		注释：# -*- coding: utf-8 -*-告诉python解释器，按照utf-8读取源代码
		格式化：%用来格式化字符串
			常见占位符：%d 整数%f 浮点数%s字符串%x十六进制数
				eg:'hello,%s,成绩提高了%.2f%%' %('小明',23.342)	
			format()方法
				eg:'Hello,{0},成绩提高了{1:.2f}%'.format('xiaoming ,23.342')
6, list()列表数据类型(相当于数组)		
		追加元素：classmates.append('') classmates.insert(index,'')
		删除元素：classmates.pop() classmates.pop(index)
		tuple()和list()类似都是python内置的有序集合，但是一旦初始化无法更改，没有append、insert、pop方法
			特别：只有一个值时，末尾一定要加逗号 (2,)
7，if判断：只要非零数值、非空字符串、非空list就判断为True
		在python中str类型和int类型不能够直接比较eg if 200>'100':
8，循环：for  in 针对list和tuple
		while 中break循环过程中直接退出循环和continue提前结束本轮循环，直接开始下一轮循环，都必须配合if语句使用
9，dict键值储存d={'Michale':95,'lee':85,'lucy':78}  print(d['lee']	)	
			判断key是否存在 方法一：'Michael' in d 方法二： d.get('Michael')
			添加：d['Jack']=75  直接添加
			删除：d.pop('Jack')   使用pop方法
			注意：dict内部存放的顺序和key放入的顺序是没有关系的
			和list比较，dict特点：查找和插入的速度极快，不会随着key的增加变慢，但是需要占用大量内存，内存浪费多，是用空间换时间的方法
			key：是不可变的，通过hash算法计算位置，只可以用字符串和整数等，不可以用list
10，set:创建set需要一个list作为输入的集合s=set([1,3,4,5,3,4]),
			添加元素：add(key)
			删除元素: remove(key)
			交集，并集 s1&s2 ;s1|s2
			
11，不可变对象：对于不可变对象，调用对象自身的任意方法，也不会改变改对象自身的内容。相反，这些方法会创建新的对象并返回。
		eg：'abc'.replace('a','A')
12,内置函数：
		abs()
		max() arguments可以是多个参数，也可以是list、tuple，set
		int()
		bool()
		float()
		str()
		hex()整数转换十六进制数
13，自定义函数：def return关键字
			空函数 ：def nop():    pass
			对参数类型做检查
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x<0:
		return -x
	else:
		return x
			python函数返回多个值其实就是返回一个tuple
			参数：位置参数
			默认参数：默认参数必须指向不变对象
			可变参数：在参数前加*，参数则会收到一个tuple
			关键字参数：def  person(name,age,**kw):   **kw 传入一个dict
			命名关键字参数：def person(name,age,*,city,address):  *后只接收city、address作为关键字参数
			在python中参数 传入的顺序是：必选参数、默认参数、可变参数、命名关键字参数、关键字参数
14，切片
			

		
		
		
		
		
		
		