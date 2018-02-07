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
    songout.write(x + "\n")

end = time.time()

print (end - start)