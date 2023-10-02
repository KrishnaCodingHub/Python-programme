with open('std.txt','w+') as f:
    f.write('krishna kushwaha')
    f.seek(0)
    print(f.read(3))
    print(f.read())
    print('is closed ', f.closed)
    
print('is closed ', f.closed)


