import re
matcher=re.finditer('[abc]','a7c@kyz')
count=0
for match in matcher:
    
    print('start index ', match.start(), ' **** matxhed str :', match.group() )
    count=count+1
print ('total : ', count )