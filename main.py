# -*- coding: utf-8 -*-
import csv

kanaListFileName = './list.txt'
dataFileName="./data.txt"
kanaList = {}
results=[]

with open(kanaListFileName, newline='',encoding='utf-8') as f:
    reader = csv.DictReader(f,delimiter = '\t')
    data = list(reader)
    for line in data:
        kanaList[line['kana']]='['+line['token']+']'
    # print(kanaList)

kanaList=str.maketrans(kanaList)

with open(dataFileName,encoding="utf-8") as f:
    reader= csv.reader(f,delimiter = '\t')
    for line in reader:
        # for kana,token in kanaList.items():
        #     temp=line[1].replace(kana,token)
        temp=line[1].translate(kanaList)
        results.append(line[0]+'\t'+temp+'\n')

with open('./out.txt','w',encoding='utf-8') as outFile:
    for line in results:
        outFile.write(line)