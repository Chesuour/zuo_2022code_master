# zuo_2022code_master

start 2022/8/3
written at Suzhou，Mobvoi，avatar group

Zuochengyun leetcode  written by python. Only for learning, Only for me.
Before finish 100+ leetcode by myself，but unable to summarize solutions to similar problems, 
this hub records my learning process to motivate myself and witness my growth.

2022/8/3  大厂面试100题 class 0 
1. CoverMaxPoint
2. MinSwapStep
3. TargetSum （recurrence ways，better ways need study 算法数据体系结构班）

2022/8/4 算法和数据结构体系班 
1. RobotWalk (three ways) 
    i) recurrence ways 
    2) space --> time
    3) dp solution
    
2022/8/5 算法和数据结构体系班 
1. CardsInline (three ways)
grilfriend comes to find me 

2022/8/8 算法和数据结构体系班 
1. 背包问题 two ways
2. ConvertToLetterString 力扣有原题

2022/8/9 算法和数据结构体系班 
1. ConvertToLetterString recurrence ways
2. TicketsToSpellWord strat

2022/8/10 算法和数据结构体系班 
TicketsToSpellWord strat 暴力递归、暂放，有点迷糊，看完回头写

2022/8/13
Drive 车辆调度问题  暴力递归和动态规划两个方法，动态规划有点小问题。

2022/8/14 程序员面试指南书
MatrixMin Path、LessExchangeCoin 
发现了一个困扰我好多天的问题
"""
=============================================================================================
PAY ATTENTION!!!!!!!!!!

n = 3
m = 3
dp = [[0] * n] * m
dp[0][1] = 1
print dp
# output:
# [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
matrix = [array] * 3
也就是说matrix = [array] * 3操作中 只是创建3个指向array的引用 所以一旦array改变matrix中3个list也会随之改变。
那如何才能在python中创建一个二维数组呢
例如创建一个3*3的数组
方法1 直接定义

[py]matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]][/py]

方法2 间接定义

matrix = [[0 for i in range(3)] for i in range(3)]
"""
