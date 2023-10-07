# To know current working directory name 
import os
cwd=os.getcwd()
print('current parrent working dir name :', cwd)

# To create new dir 
# os.mkdir('newdir')
# print('new dir created ')

# To create new dir at specify dir
# os.mkdir('newdir/subdir')
# print('Sub directory created successfully')

# To create multiple Dirs
# os.makedirs('dir10/dir20/dir30/dir40/dir50')
# print('Directories created Successfuly ')

# To remove Dir
# os.rmdir('newdir')
# print('task completed ')

# To remove multiple dir
# os.removedirs('dir1/dir2/dir3/dir4/dir5')
# print('task completed ')

# To rename dir 
# os.rename('dir10','dir100')
# print('task completed ')

# To know contents of the dir 
# list2=os.listdir('dir100')
# print(list2)
# print('total contents', len(list2))

# To know content of Sub dir
# x=os.walk('dir100')
# print(next(x))
# print(next(x))

# To Know current working directory
# x=os.walk('.')
# for dir,subdir,filename in x:
#     print('Current Dir',dir)
#     print('Subdir Name : ', subdir)
#     print('file Name :', filename)


# To get file info
fileinfo=os.stat('emp2.csv')
print(fileinfo)

