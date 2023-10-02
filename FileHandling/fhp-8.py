f=open("student.txt","r")
f2=open("student_out.txt","w")
line=f.read()
f2.write(line)
f.close