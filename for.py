"""
    for 语句 适合执行预定次数
    while 语句  适合根据条件循环执行
    for 变量列表 in 可迭代对象
        语句块1
    else
        语句块2
"""
str01 = "我是苏大强！"
# item 存储的是字符串中每个字符的地址
for item in str01:
    print(item)
# 整数生成器，range(开始值，结束值，间隔)
# for +range :更善于执行预定次数
for item in range(1, 5, 2):
    print(item)
# 折纸十次
thickness = 0.001
for item in range(10):
    thickness *= 2
print(thickness)
# 累加1-100的和
num = 1
sum_val = 0
# for num in range(101):
#     sum_val += num
# print(sum_val)
# 累加偶数
for num in range(2, 101, 2):
    sum_val += num
print(sum_val)
# 累加10-36之间的和
sum_val = 0
for num in range(10, 37):
    sum_val += num
print(sum_val)
