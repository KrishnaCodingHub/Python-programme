import re
matcher =re.finditer('k', '012kasw11k')
for match in matcher:
    print(match.start(), match.span(), match.group())
    