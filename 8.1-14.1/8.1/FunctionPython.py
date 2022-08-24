# 导入自定义函数PrintFunction包
# 使用as关键字能够给模块指定别名, 代码中将采用别名.函数 调用
# import PrintFunction * 导入模块中的所有函数
import PrintFunction
# 也可以单独导入函数
from PrintFunction import info_user

# 定义函数 def 关键字
# def hello_user(user_string):
#     print(user_string.title())


# 定义函数时可以赋予形参默认值
def hello_user(user_string="default", user_age="default"):
    print("user_string: " + user_string + ", user_age: " + user_age)
    return True


# 定义位置数量形参函数 *
# * 告诉Python创建一个名为string_user的空元组, 调用函数是给多少个实参便创建长度为多少的元祖
def print_user(*string_user):
    print(string_user)


# 定义一个已知参数位置, 和未知的函数
# def print_user( parameter_string, *string_user):
#     print(string_user)

# 定义形参为字典的函数 **
# ** 告诉Python形参为字典, 需要创建一个空字典来存储
# def info_user(**string_user):
#     for key, value in string_user.items():
#         print("key: " + key + ", value:" + value)

# hello_user("hello")

# hello_user()
boolean = hello_user("hello", "11")
print(boolean)
print("------------")

print_user(1, )
print_user(1, 2)
print_user(1, 2, 3)

# user_info = {"age": "11", "name": "LiZ", "like": "music"}
# 调用PrintFunction包中的info_user函数
# PrintFunction.info_user(age="11", name="LiZ")
info_user(age="11", name="LiZ")
