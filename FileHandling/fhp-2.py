import os
fname= input('enter a file name : ')
if os.path.isfile(fname):
    print(f'{fname} is avialble')
    lcount = 0
    wcount = 0
    ccount=0
    f=open(fname,'r')
    # print(f.read())
    for line in f:
        lcount=lcount+1
        words=line.split()
        wcount=wcount+len(words)
        ccount=ccount+len(line)
    print(' No of line', lcount)
    print(' No of words ' , wcount)
    print(' No Charcter ', ccount)
    
else:
    print('file not avialable')
    # print()
    f=open(fname,'w+')
    f.write('i love programmimg \n I love Cooking \n I love reading \n')
    f.close()
    