# -*- coding: utf-8 -*-
# @Time : 2022/2/14
# @Author : RelikRan
"""
list 列表  序列数据类型  类似tuple元组   他们之见区别：元组是不可变的  list可变数据类型
1、定义：列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
    列表的类型可以为任意类型
    列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）
2、如何获取列表中的元素  切片
    和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
    列表截取的语法格式如下：
        变量[头下标:尾下标]
    索引值以 0 为开始值，-1 为从末尾的开始位置。
3、修改列表的元素值
4、删除列表元组或列表   del pop remover
5、list常用的运算符    + * in/not in
6、嵌套
7、list常见内置函数  max min len
    添加元素
        append() 列表最后添加新元素（追加鑫元素）
        extend() 追加多个元素
        insert() 制定索引位置，添加元素

    删除元素
        pop（index=-1） 默认移除最后一个元素
        列表允许多个重复的值  可以
        remove 根据指定的值进行移除，移除列表中的某个值的一个匹配项
"""
list1 = ["adbc", 'python', 123]
print(list1)            # 输出完整列表    ['adbc', 'python', 123]
print(type(list1))      #  输出类型     <class 'list'>
list2 = []
print(list2)
print(type(list2))

# 获取列表中的元素  切片
print (list1[0])         # 输出列表第一个元素
print (list1[1:3])       # 从第二个开始输出到第三个元素
print (list1[2:])        # 输出从第三个元素开始的所有元素

# 修改列表的元素值
list1[-1] = '456'
print(list1)

# 删除列表元组或列表   del
del list1[-1]
print(list1)
list3 = ['abcdef']
# del list3
# print(list3)  # NameError: name 'list3' is not defined

# 5、list常用的运算符    + * in/not in
new = ['A','b']
name211 = list1 + new
print(name211)
name212 = name211 * 2
print(name212)

# 6、嵌套
list4 = ['1','2', ['3',"AA"]]
print(list4[-1][1])

list5 = [1, 2, 3, 4]
# 实现添加新元素，返回None
list5.append(5)
print(list5)
newlist5 = list5.append(5)
print(newlist5)     # None
list5.extend([6, 7, 8, 9])
print(list5)    #   [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

list5.append([6, 7, 8, 9])
print(list5)    # [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, [6, 7, 8, 9]]

list5.insert(0, 0)
print(list5)

list6

