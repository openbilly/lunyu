# -- coding: utf-8 --

import json
import os


fileopen = open("org.txt", 'r', encoding='utf-8')
file = fileopen.read()
#print(type(file))
file2 = file.replace(r'<p class="calibre4"><span class="kindle-cn-specialtext-bg">原文</span> ', r'{"originalText": "' )
file3 = file2.replace('</p>\n\n<p class=\"calibre4\"><span class=\"kindle-cn-specialtext-bg\">直解</span> ', r'", "explain": "')
file4 = file3.replace('</p>\n', r'"},')
file5 = file4.replace('</p>', r'"}')

output = "./txt.json"
file200 = open(output, 'w', encoding='utf-8')
file200.write(file4)
fileopen.close()
file200.close()
