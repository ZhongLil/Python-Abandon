# 类似JAVA中基本上用不到的Scanner()
# 使用input()函数获取到用户的输入
# edit = input("Please Edit: ")
# print("Edit: " + edit)

# 获取用户输入的整形数据需要将获取到的字符串进行int()函数转换, 类似Scanner中的Scanner.nextInt()函数
# nextInt()函数底层关键方法Integer.value(String)
# num_edit = input("please Edit num: ")
# print(int(num_edit))

# while语句
current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1

# 使用break也能达到效果
# continue使用方法一致
print("-----------")
current_num = 1
while True:
    if current_num > 5:
        break
    print(current_num)
    current_num += 1