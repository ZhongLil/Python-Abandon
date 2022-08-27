import InfoClass

# from info_class import InfoClass


# 导入model的时候会报参数错误
# 需要导入InfoClass模块中的InfoClass类
class SonClass(InfoClass.InfoClass):

    def __init__(self, name, age, like, sex):
        super().__init__(name, age, like)

        self.sex = sex

# 重写父类方法output_info方法

    def output_info(self):
        print("name: " + self.name + ", age: " + self.age + ", like: " +
              self.like + ", sex: " + self.sex)


# 一个模块中可以存在多个类
class Language():

    def __init__(self, language) -> None:
        self.language = language

    def output_info(self):
        print("language: " + self.language)