# -- coding: utf-8 --
# 用来输出张居正《四书直解：论语》

import json
import os
import time

file = open("zhangjuzheng.json", 'r', encoding='utf-8')
data = file.read()
chapters = json.loads(data)
#print("数据类型：")
#print(type(data))
#print(type(chapters))
# print(books[0])
#print(type(chapters[0]))

"""
以下如果不按《论语》的原分段，是可行的
for chapter in chapters:
    paragraphs = chapter.get('paragraphs')
    for paragraph in paragraphs:
        print("原文： " + paragraph.get('originalText'))
        print("直注： " + paragraph.get('explain'))
#以上
"""
#以上

for chapter in chapters:
    print(chapter.get('chapterName'))
    print(chapter.get('introduction'))
    i = int(1)
    for paragraph in chapter.get('paragraphs'):
        print (i)
        for sents in paragraph:
            print ("# 原文： " + sents.get('originalText'))
            print ("直解： " + sents.get('explain'))
        i += 1
