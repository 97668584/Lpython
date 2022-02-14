# -*- coding: utf-8 -*-
# @Time : 2022/1/22
# @Author : RelikRan
import keyword
print(keyword.kwlist)

print ("hello world!!!")
print ("欢迎q加入!!!")

isOver = True
if isOver:
    print('开始学习')
    print('python')
else:
    print('继续学习，加油~~~')


# 导入
# import module2
# print('212期班级人数：',module2.class212_num)
# module2.learn_01()

'''导入某个模块具体某个函数及数据'''
# from module2 import class212_num,learn_01
# print(class212_num)
# learn_01()

'''导入某个某块所有函数及数据'''
# from module2 import *
# learn_01()
# learn_02()
# print(class212_num)
#
# from module2 import learn_01 as d
# from class002.module3 import learn_01
# d()
# learn_01()

# from class002.module3 import learn_01
# learn_01()

# import class002.module3
# class002.module3.learn_01()

from class002 import module3
module3.learn_01()