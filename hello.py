#!/usr/bin/python
# -*- coding: UTF-8 -*-
print('你好，世界')
print('按enter键，\n')
# raw_input("按下 enter 键退出，其他任意键显示...\n")
''' 注释？'''
print ord('a')
def deduplication(self, nums):#找出排序数组的索引
    print(len(nums))
    for i in range(len(nums)):
        if nums[i]==self:
            return i
    i=0
    for x in nums:
        print(x)
        if self>x:
            i+=1
    return i
print(deduplication(5, [1,3,5,6]))
raw_input("继续还书请输入：c 返回主菜单请输入：b ：")