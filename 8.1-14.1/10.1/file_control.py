# 输出整个文本内容
filename = "F:\project\python\Python-Abandon\8.1-14.1\\10.1\copy.txt"
num = []
with open("F:\project\python\Python-Abandon\8.1-14.1\\10.1\pi.txt"
          ) as file_object:

    # contents = file_object.read()
    # print(contents)

    # 一次读取一行
    for line in file_object:
        num.append(line.rstrip())
        print(num)
        # 输出到文件
        with open(filename, "a") as output_file_object:
            output_file_object.write(line)
