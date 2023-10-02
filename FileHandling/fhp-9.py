f=open('student.txt','r')

print('current position : ', f.tell())
# print(f.read())
print(f.read(7))
print('current position : ', f.tell())
print('moved : ',f.seek(12))
print('current position : ', f.tell())
print(f.read(7))

f.close