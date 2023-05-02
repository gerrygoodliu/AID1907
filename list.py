"""
    list 列表
        由一系列变量组成的可变序列容器
"""
# 创建空列表
list01 = []
list01 = list()
# 默认值
list02 = ["悟空", 100, True]
list02 = list("我是物理大神")
# 获取元素
# 索引
print(list02[2])
# 切片
print(list02[-4:])
# 添加元素 append
list02.append("八戒")
print(list02)
# 插入 insert(指定位置，数据)
list02.insert(2, 500)
print(list02)
# 删除元素
# 根据元素删除
list02.remove("是")
print(list02)
# 根据位置删除
del list02[0]
print(list02)
# 定义元素   ，可以增删改查
# 切片
del list02[1:3]
print(list02)
# 修改
list02[1:3] = ["a", "b"]
print(list02)
# 遍历列表  获取所有元素
for item in list02:
    print(item)
# 倒序获取所有元素
# list02[::-1]通过切片拿元素，会重新创建列表
# for item in list02[::-1]:
#     print(item)
for item in range(len(list02)-1,-1,-1):
    print(list02[item])
print("空")
for i in range(-1,-len(list02),-1):
    print(list02[i])