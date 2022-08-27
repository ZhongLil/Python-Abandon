import json
# 向json文件中写入
filename = "F:\project\python\Python-Abandon\8.1-14.1\\10.1\data.json"
with open(filename, "w") as json_object:
    json.dump("username", json_object)

# 从json文件中读取
with open(filename) as json_object:
    print(json.load(json_object))