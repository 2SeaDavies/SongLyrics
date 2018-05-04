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
#create an array of line lengths
while length > 0:
    y = random.randint(3,10)
    lines.append(y)
    length -= y
    print(length)


lol = []

#populate an array of words from the dictionary
for x in MyFile.read().split():
    lol.append(x)

#create an array and start a timer
words = []
start = time.time()
# add random words to the array
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