import os
fname=input('Enter a file name : ')
if os.path.isfile(fname):
    print(f'file {fname} is aviable')
    print('*'*50)
    print(open(fname).read())
    print('*'*50)
else:
    print(f'file {fname} is not aviable ')