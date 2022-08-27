import InfoClass
import SonClass

# newObject
# JAVA Class myClass = new Class();
# myClass.xxxx

my_info = InfoClass.InfoClass("LiZ", "11", "music")
my_info.output_info()

# 初始化子类
son_class_info = SonClass.SonClass("LiZ", "11", "music", "man")

my_language = SonClass.Language("China")

# 修改对象my_info中的属性
print("-------------------------")
my_info.name = "LiZ Change1"
my_info.output_info()

print("-------------------------")
son_class_info.output_info()

print("-------------------------")
my_language.output_info()