# Python字典 与JAVA Map集合类似, key-value
# map_0 = {key : value, key : value, ..........}
# 访问对应的value map_0[key]

map_0 = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(map_0["key1"])
print(map_0["key2"])
print(map_0["key3"])

# 向字典中添加元素 map_0[key] = value
# 可创建一个空字典 mao_1{}, 以以上方法向其中添加元素
map_0[1] = 1
map_0[2] = 2
print(map_0)

# 修改key对应的value
print("\n---------------")
map_0["key1"] = "change1"
print(map_0["key1"])

# del语句 删除键值对
del map_0["key2"]
print(map_0)

# 遍历字典需使用items()函数来遍历字典, 类似JAVA中通过Map.entrySet使用iterator遍历key和value
print("\n---------------")
for key, value in map_0.items():
    print("key: " + str(key))
    print("value: " + str(value))

# 使用keys()函数遍历字典中的key, 类似JAVA中使用Map.keySet()来遍历Map中的Key
# 使用values()函数能遍历字典中的value, 类似JAVA中使用Map.values()来遍历Map中的value
# 同样的通过keys()函数获取到的集合也能通过sorted()函数进行排序
print("\n---------------")
for key in map_0.keys():
    print(key)

# map_0中包含整形key, 所以会报错
# for key in sorted(map_0.keys()):
#     print(key)

# 同样字典也能嵌套使用类似JAVA中:
# List.add(Map)
# Map.put("list1", List)
# Map.put("list2", List)