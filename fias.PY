def fread(f):
    s = f.readline()
    return s[:len(s)-1:]

import os
import httpx
from dadata import Dadata
token = 'd17ca138e3bf51a00bceb2daf6300bd45181ee75'
secret = 'a0108d1241225db0f2f2b726e1e61d400d2cf250'
dadata = Dadata(token, secret)
f = open('in.txt')
operation = fread(f)
source = fread(f)
if operation=='clean':
    try:
        result = dadata.clean(name="address", source=source)
    except httpx.HTTPStatusError as exc:
        result = {
            'error': exc.response.status_code,
        }
elif operation=='find_by_id':
    result = dadata.find_by_id(name="address", query=source)
    try:
        result = result[0]
    except IndexError:
        result = {
            'error': 0,
        }
else:
    result = {
        'error': '',
    }
dadata.close()
f.close()
f = open('out.txt', 'w')
f.write('operation='+operation+'\n')
f.write('source='+source+'\n')
for index,value in result.items():
    tp = type(value)
    if tp==int:
        value = str(value)
    elif tp!=str or index=='source':
        continue
    f.write(index+'='+value+'\n')
f.close()
os.remove('in.txt')
