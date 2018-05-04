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
#open the files
MyFile=open('lyrical.txt','r')
words={}
count=0

songout = open('Output.txt','w')


from collections import defaultdict

#write the words, their counts and sort the words by count
def sorter():
    counts = defaultdict(int)
    for x in MyFile.read().split():
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])

#time how long it takes
start = time.time()

songout.write('\n'.join('%s %s' % x for x in sorter()))
end = time.time()

print (end - start)