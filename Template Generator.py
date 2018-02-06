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
MyFile=open('Output.txt','r')
words={}
count=0

oneN=open('1n.txt','r')
twoN=open('2n.txt','r')
threeN=open('3n.txt','r')
fourN=open('4n.txt','r')



songout = open('Output.txt','w')


from collections import defaultdict


def leaders():
    counts = defaultdict(int)
    for x in MyFile.read().split():
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])


start = time.time()
songout.write('\n'.join('%s %s' % x for x in leaders()))
end = time.time()

print (end - start)