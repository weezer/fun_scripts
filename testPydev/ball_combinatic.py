#!/usr/bin/python
# -*- coding: utf8 -*-

num = 10


# 小球数量可以为0, 列出所有的组合,不能有重复,比如1,2,1 and 1,1,2
def dfs1(start, target, res, result):
    if start == target:
        print res
        result.append(res)
        return
    for i in range(1, target):
        if len(res) > 0 and i > res[-1]:
            continue
        copy_res = res[:]
        copy_res.append(i)
        dfs1(1, target-i, copy_res,result)

_result = []
# dfs1(1, num+1, [], _result)
# print len(_result)


# 小球数量可以为0分割,一共有多少种拼凑方式
def dp_1(num):
    # 0个球,不管放多少盘子都是1, 0个盘子,不管多少个球都是0
    matrix = [[0 for i in range(num+1)] for j in range(num+1)]
    for i in range(num+1):
        matrix[0][i] = 1

    # i为小球数量, j为框的数量
    for i in range(1, num+1):
        for j in range(1, num + 1):
            if i >= j:
                matrix[i][j] = matrix[i][j-1] + matrix[i-j][j]
            else:
                matrix[i][j] = matrix[i][j-1]
    print matrix[i][j]

# dp_1(num)


# 框种小球数量不能为0, 不能有重复的, k为小球数量,v为筐数量
def dfs_2(k, v):
    if k == v:
        return [1] * v
    if k < v:
        return 0

    _result = []

    def dfs2(start, target, step, res, result):
        if step == 0:
            if target == start:
                print res
                result.append(res)
            return
        for i in range(1, target):
            if len(res) > 0 and res[-1] > i:
                continue
            if step <= target - i:
                copy_res = res[:]
                copy_res.append(i)
                dfs2(1, target - i, step - 1, copy_res, result)
    dfs2(1, k, v, [], _result)
    print len(_result)

dfs_2(num+1, 3)


# 筐中小球数量不能为0, 有多少种拼凑方式?
def dp_2(k, v):
    matrix = [[0 for i in range(k+1)] for j in range(k+1)]
    for i in range(k+1):
        matrix[i][i] = 1

    for i in range(1, k+1):
        for j in range(1, k+1):
            if i >= j:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-j][j]

    # for i in range(1, k+1):
    #     print matrix[i]
    print matrix[k][v]


dp_2(num, 3)