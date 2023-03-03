# -- coding: utf-8 --

import json
import os


fileopen = open("zhangjuzheng.json", 'r', encoding='utf-8')
file = fileopen.read()
dic = json.loads(file)
jsonOutput = json.dumps(dic, ensure_ascii=False, indent=2,)
output = "./zhangjuzheng.standard.json"
file2 = open(output, 'w', encoding='utf-8')
file2.write(jsonOutput)
fileopen.close()
file2.close()

#file = open('zhangjuzheng.json', 'r', encoding='utf-8')
#date = json.load(file)
#print(date)
