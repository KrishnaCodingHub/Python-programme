f=open('abc.txt','w')
# d=['100':1000, '200':2000, '300':3000]
d= {'A': 1000, 'B': 2000, 'C': 3000}
f.writelines(d)
print("data written successfully")
f.close()