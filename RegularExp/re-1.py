import re
pattern=re.compile('ba')
matcher=pattern.finditer('ababababasasbbba')
count=0
for match in matcher:
    count+=1
    print('Start Index :',match.start(),'*****','end Index :',match.end(),'******', match.group())
    print('the number of count :',count)
