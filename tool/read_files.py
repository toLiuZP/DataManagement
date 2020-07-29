
import os

build_file = r".\output\build_script.sql"


path =r"C:\LiuZP\00. CodeBase\Aspira\insights-sql\SourceCode\Databases\ASPIRAONE_DASHBOARD_MART\StoredProcedures1902"    #指定需要读取文件的目录
files =os.listdir(path) 
files.sort() 
file_list = []                  
for file_ in files:

    if not os.path.isdir(path +file_): 
        f_name = str(file_)
        print(f_name)

        file_list.append(f_name) 
        #with open(path + '\\' + file_, 'r', encoding="utf") as f:
        with open(path + '\\' + file_, 'r') as f:
            test_txt = f.read()
            test_txt += '\n'
        with open(build_file, 'a') as file_object:
            file_object.write(test_txt)




#print(file_list) 