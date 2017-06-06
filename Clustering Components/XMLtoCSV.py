'''
Run this script with the name of the easyUML .cdg file as the 1st argument
It will output a csv file for weka to use.
Created on May 23, 2017

@author: Jeremy Albert
'''
import sys
row=0
col=0
src=[]
tar=[]
print ("Opening XML file: "+sys.argv[1])
print ("Writing to CSV file: CSVdata.csv")

with open(sys.argv[1]) as r:
    for line in r:
        line=line.strip('\n')
        line=line.strip('    ')
        data=line.split(' ')
        if data[0]=="<UseRelation":
            if data[1] not in src:
                src.append(data[1])
            if data[2] not in tar:
                tar.append(data[2])
        if data[0]=="<HasRelation" or data[0]=="<ImplementsRelation" or data[0]=="<isRelation":
            data[3]=data[3].strip('>')
            data[3]=data[3].strip('/')
            if data[2] not in src:
                src.append(data[2])
            if data[3] not in tar:
                tar.append(data[3])
                    
table=[[0 for x in range(len(tar))] for y in range(len(src))]

with open(sys.argv[1]) as r:
    for line in r:
        line=line.strip('\n')
        line=line.strip('    ')
        data=line.split(' ')
        if data[0]=="<UseRelation":
            row=src.index(data[1])
            col=tar.index(data[2])
            table[row][col]+=1
        if data[0]=="<HasRelation" or data[0]=="<ImplementsRelation" or data[0]=="<isRelation":
            data[3]=data[3].strip('>')
            data[3]=data[3].strip('/')
            row=src.index(data[2])
            col=tar.index(data[3])
            table[row][col]+=1
         
w=open("CSVdata.csv",'w')
w.write("Name")
for i in range(len(tar)):
    cleaned=tar[i].split('=')
    w.write(','+str(cleaned[1]))
        
for i in range(len(src)):
    cleaned=src[i].split('=')
    w.write('\n'+str(cleaned[1])+',')
    for j in range(len(tar)):
        w.write(str(table[i][j]))
        if (j+1 != len(tar)):
            w.write(',')
