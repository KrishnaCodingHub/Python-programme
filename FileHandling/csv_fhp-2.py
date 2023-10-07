import csv
with open('emp7.csv', 'a+', newline='')as fname:
    w=csv.writer(fname)
    fname.seek(0)
    data=list(csv.reader(fname))
    colname=['Eno','Ename', 'Ephone' ]
    for col in data:
        if colname not in col[0]:
            w.writerow(colname)
    while True:
        eno=int(input('Enter employee No :'))
        ename=input('Enter employee Name :')
        ephone=int(input('Enter employee Phone :'))
        w.writerow([eno,ename,ephone])
        print ('Data Inserted Successfully ')
        option=input('Do you want more data [yes/No] ? ')
        if option in ['NO','no','n','No']:
            break
        
    fname.seek(0)
    print('*'*50)
    w=csv.reader(fname)
    data=list(w)
    for row in data:
        # print(row)
        for col in row:
            print(col, '\t', end='')
        print('')
    print('*'*50)

    