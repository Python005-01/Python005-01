基本数据类型: int str tuple list dict set

不可变数据类型: int str tuple 

可变数据类型:list dict set

有序:list tuple

无序:dict set

1.int整型
-
In [2]: num=1

In [3]: print(num)

In [5]: type(num)

Out[5]: int

2.str(字符串)
-

In [7]: astr="123456"


打印astr变量
-
In [8]: print(astr)

123456


查看数据类型为字符
-
In [9]: type(astr)

Out[9]: str
切片
-
In [10]: astr[0:]

Out[10]: '123456'

切片从下标0到第1个字符
-
In [11]: astr[0:1]

Out[11]: '1'

切片从下标0到第2个字符
-
In [12]: astr[0:2]

Out[12]: '12'

切片反向排序
-
In [15]: astr[-1::-1]

Out[15]: '654321'

切片步长为2
-
In [18]: astr[0::2]

Out[18]: '135'

查看字符长度
-
In [19]: len(astr)

Out[19]: 6

3.list(列表)
-
In [24]: alist=['a', 'b', 'c', 'd', 'e']

打印list
-
In [25]: print(alist)

['a', 'b', 'c', 'd', 'e']

查看类型为list
-
In [26]: type(alist)

Out[26]: list

遍历list
-
In [28]: for i in alist:

   ...:     print(i)

   ...:
a

b

c

d

e

添加元素
-
In [29]: alist.append("f")

In [30]: alist

Out[30]: ['a', 'b', 'c', 'd', 'e', 'f']

扩展元素
-
In [31]: alist.extend([1,2,3,4,5,6])

In [33]: alist

Out[33]: ['a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6]

插入元素
-
In [13]: alist.insert(0,"aa")

In [14]: alist

Out[14]: ['aa', 'a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6]

In [15]: alist.insert(2,"bb")

In [16]: alist

Out[16]: ['aa', 'a', 'bb', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6]

修改元素
-
In [17]: alist[0]='aaa'

In [18]: alist

Out[18]: ['aaa', 'a', 'bb', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6]

In [19]: alist[3]='bbb'

In [20]: alist

Out[20]: ['aaa', 'a', 'bb', 'bbb', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6]


4.tuple
-

元组就是不变的list 不能添加元素
-
In [36]: atuple=(1,2,3,4,5,6)

In [37]: atuple

Out[37]: (1, 2, 3, 4, 5, 6)

因为元组是不该被所以,不能添加元素


#所以出现报错,元组是不可变的
In [22]: atuple.append('a')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-22-90bec10dc171> in <module>()
----> 1 atuple.append('a')

AttributeError: 'tuple' object has no attribute 'append'
5.dict(字典)
-
In [49]: adict = {"a":1, "b":2, "c":3}

查看类型为dict
-
In [50]: type(adict)

Out[50]: dict

打印dict
-
In [51]: print(adict)

{'a': 1, 'b': 2, 'c': 3}

根据下标获取元素2
-
In [53]: adict["a"]

Out[53]: 1

In [54]: adict["b"]

Out[54]: 2

In [55]: adict["c"]

Out[55]: 3

In [56]: len(adict)

Out[56]: 3

In [58]: adict.items()

Out[58]: dict_items([('a', 1), ('b', 2), ('c', 3)])

In [59]: adict.keys()

Out[59]: dict_keys(['a', 'b', 'c'])

In [60]: adict.values()

Out[60]: dict_values([1, 2, 3])

In [23]: adict = {"a":1, "b":2, "c":3}

字典key是不可变的 
-
In [24]: adict[('a','b','c')]="aa"

In [25]: adict

Out[25]: {'a': 1, 'b': 2, 'c': 3, ('a', 'b', 'c'): 'aa'}

Key赋值数据类型可变的list就是出现报错
In [26]: adict[['a','b','c']]="aa"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-26-a803d9cb865f> in <module>()
----> 1 adict[['a','b','c']]="aa"

TypeError: unhashable type: 'list'


6.set集合
-

In [65]: aset = set={1,3,2,1,3,2}

In [66]: type(aset)

Out[66]: set

In [67]: print(aset)
{1, 2, 3}



