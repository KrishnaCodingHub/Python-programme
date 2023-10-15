import re
# matcher=re.finditer('[^abc]', 'ab5xyz@kskdsd')
matcher=re.finditer('[^a-zA-Z0-9]', 'ab5x4Zz@kLk2dAd')
count=0
for match in matcher:
    print('start index :', match.start(), 'match str : ',match.group())
    count= count+1
print('total : ', count)
print(re.search(r'G[^e]', 'Greeks')) 