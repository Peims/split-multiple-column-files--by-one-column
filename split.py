#!/usr/bin/env python
#created by Maosong Pei
 import os
from sys import argv

a=open(argv[1],"rt")
dic={}
while True:
    lineL=a.readline()
    if not lineL:
        break
    line=lineL.strip().split("\t",1)
    if line[0]=="pattern":
        continue
    elif line[0] not in dic:
        dic[line[0]]=[line[1]]
    else:
        dic[line[0]].append(line[1])

for k,v in dic.items():
    name=k
    with open(k,"wt") as r:
        r.write("ID-1"+"\t"+"ID-2"+"\t"+"ID-3"+"\t"+"ID-4"+"\n")
        for val in v:
            r.write(k+"\t"+val+"\n")
a.close()