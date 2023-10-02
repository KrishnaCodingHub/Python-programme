import os
statics=os.stat('fhp-1.py')
print(statics.st_size)
print(statics.st_mtime)