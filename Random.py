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



import time
import random
MyFile=open('lyrical.txt','r')
words={}
count=0

songout = open('Output.txt','w')


from collections import defaultdict
lol = []


for x in MyFile.read().split():
    lol.append(x)



start = time.time()

for i in range(100):
    number = random.randint(0, len(lol))
    print(lol[number])




end = time.time()

print (end - start)