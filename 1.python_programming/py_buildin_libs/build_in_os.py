import os
from datetime import datetime

# print(os.getcwd())
# print(os.listdir())
#os.mkdir('test_dir')
#os.chdir('.\\test_dir')
#print(os.getcwd())
#os.makedirs('.\\test_dir\\sub_dir_1')

#os.chdir('.\\test_dir')
#os.rename('sub_dir_1', 'inside_dir')
# print(os.getcwd())
# print(os.listdir())
# print(os.stat('main_file').st_size)
# mod_time = os.stat('main_file').st_mtime
# print(datetime.fromtimestamp(mod_time))

print(os.getcwd())
# os.chdir('.\\py_buildin_libs')
# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print("Current directory path: ", dirpath)
#     print("Directories: ", dirnames)
#     print("Files: ", filenames)
#     print()

print(os.environ.get('USERNAME'))