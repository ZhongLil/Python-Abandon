# ython数组&集合
str_list = ['test1', 'test2', 'test3']
print(str_list)
print(str_list[1].title())
print(str_list[-1])

# 元素操作增删改查
str_list[0] = "change1"
print(str_list[0])

str_list.append("addString1")
print(str_list)
# 可以构建一个空数组, 不用定义数组长度, append函数可以进行数组长度动态调整
# (待确认: del函数删除元素后数组长度是否会动态减少)
# 逻辑推测: 数组长度不会减少, 会由null占位
str_list2 = []
print(str_list2)

str_list2.append("append1")
str_list2.append("append2")
str_list2.append("append3")
print(str_list2)

# 推测错误, 删除后长度动态减少
# 注意数组下标越界
# 需要单独取出删除的元素则需要使用pop()函数
# 将删除的元素赋予变量
# stirng = str_list.pop(index)
# (未标明index时则取出最后一个元素)
del str_list2[1]
print(str_list2)
print(len(str_list2))
# 插入函数insert(index, string)
str_list2.insert(0, "btest")
print(str_list2)
print(sorted(str_list2))
