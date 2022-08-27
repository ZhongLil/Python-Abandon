# 在Python2中 需要这样写: class InfiClass(object)
class InfoClass:
    # __init__() 方法类似JAVA构造函数# __init__() 方法类似JAVA构造函数
    def __init__(self, name, age, like):
        self.name = name
        self.age = age
        self.like = like

    # 方法
    def output_info(self):
        print("name: " + self.name + ", age: " + self.age + ", like: " +
              self.like)
