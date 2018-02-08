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
MyFile=open('Wooden.txt','r')
words={}
count=0

songout = open('copytest.txt','w')


from collections import defaultdict








start = time.time()

for x in MyFile.readlines():
    for word in x:
        if word == "me":
            word.replace('me', 'baller')



MyFile=open('Wooden.txt','r')

for x in MyFile.readlines():
    print(x)
    songout.write(x)


# Read in the file
#with open('wooden.txt', 'r') as file,open("1n.txt") as n1 :
 # filedata = file.read()

# Replace the target string
#filedata = filedata.replace('ram', 'abcd')

# Write the file out again
#with open('file.txt', 'w') as file:
 # file.write(filedata)



end = time.time()

print (end - start)