f=open("student.txt","a+")
while True:
    fname=input("Enter a name :")
    f.writelines(fname)
    option=input("Do you want some data [yes/no] ?")
    if option.lower()=="no":
        break
    print ("data written successfully ")
f=open("student.txt","r")
str =f.read()
print("Student Name : ", str)
print(f.read())
print(f.read())
print(f.read())
f.close()
