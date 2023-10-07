from zipfile import *
f=ZipFile('csvfilezip.zip','w', ZIP_DEFLATED)
f.write('emp.csv')
f.write('emp2.csv')
f.write('emp3.csv')
f.close()
print('files are ziped successfuly')