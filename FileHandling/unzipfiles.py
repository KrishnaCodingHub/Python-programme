from zipfile import *
f=ZipFile('csvfilezip.zip','r',ZIP_STORED)
files=f.namelist()
for file in files:
    print(file)