# for 循环 与 JAVA Foreach相似
from audioop import avg

num_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
i = 0
for num in num_list:
    print("num:" + str(num))

# range(startIndex, endIndex)函数
# 用于创建一段连续整形数组
# 两个参数与JAVA中substring(startIndex, endIndex)相似, 从startIndex开始, 一直到endIndex(不包括endIndex)
# 输出结果:
# 1
# 2
# 3
# 4
for value in range(1, 5):
    print(value)
numbers = list(range(1, 5))
print(numbers)
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
# print(avg(squares))
print(sum(squares))

# 截取数组元素 ints[starIndex : endIndex] 与JAVAsubstring相同
print(squares[1:5])
print(squares[:5])
print(squares[1:])
for square in squares[:5]:
    print(square)
# 截取可用于复制两张表
squares_copy = squares[:]
squares_copy.append("appendstring")
print(squares_copy)
