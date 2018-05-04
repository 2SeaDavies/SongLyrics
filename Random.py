#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Craig
#
# Created:     25/11/2015
# Copyright:   (c) Craig 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#import and open the file
import time
import random
MyFile = open('lyrical.txt','r')
words = {}
count = 0



length = 200
songout = open('Output.txt','w')
lines = []

while length > 0:
    y = random.randint(3,10)
    lines.append(y)
    length -= y
    print(length)


lol = []


for x in MyFile.read().split():
    lol.append(x)


words = []
start = time.time()

for i in lines:
    line = ""
    for j in range (i):
        number = random.randint(0, len(lol))
        line+= " "
        line+= lol[number]
    words.append(line)

for k in words:
    print(k)








end = time.time()

print (end - start)