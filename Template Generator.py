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
oneN=open('1n.txt','r')
twoN=open('2n.txt','r')
threeN=open('3n.txt','r')
fourN=open('4n.txt','r')
oneA=open('1a.txt','r')
twoA=open('2a.txt','r')
threeA=open('3a.txt','r')
fourA=open('4a.txt','r')
oneV=open('1v.txt','r')
twoV=open('2v.txt','r')
threeV=open('3v.txt','r')
fourV=open('4v.txt','r')
songout = open('Output.txt','w')

Templates = open('Templates.txt','w')

start = time.time()


with open("1n.txt") as f1,open("lyrical.txt") as f2:
    words=set(line.strip() for line in f1)   #create a set of words from dictionary file

    #why sets? sets provide an O(1) lookup, so overall complexity is O(N)

    #now loop over each line of other file (word, freq file)
    for x in f2.read().split():
          #fetch word,freq
        if x in words:        #if word is found in words set then print it
            print (x)


end = time.time()




print (end - start)