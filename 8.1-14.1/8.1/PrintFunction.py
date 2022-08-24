# 定义形参为字典的函数 **
# ** 告诉Python形参为字典, 需要创建一个空字典来存储
def info_user(**string_user):
    for key, value in string_user.items():
        print("key: " + key + ", value:" + value)