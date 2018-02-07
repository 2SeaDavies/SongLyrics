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


with open("1n.txt") as n1,open("2n.txt") as n2,open("3n.txt") as n3,open("4n.txt") as n4,open("1a.txt") as a1,open("2a.txt") as a2,open("3a.txt") as a3,open("4a.txt") as a4,open("1v.txt") as v1,open("2v.txt") as v2,open("3v.txt") as v3,open("4v.txt") as v4,open("lyrical.txt") as f2:
    onenouns=set(line.strip() for line in n1)   #create a set of words from dictionary file
    twonouns = set(line.strip() for line in n2)
    threenouns = set(line.strip() for line in n3)
    fournouns = set(line.strip() for line in n4)

    #why sets? sets provide an O(1) lookup, so overall complexity is O(N)

    #now loop over each line of other file (word, freq file)
    for x in f2.read().split():
          #fetch word,freq
        if x in onenouns:        #if word is found in words set then print it
            print ("1n")
        elif x in twonouns:
            print ("2n")
        elif x in threenouns:
            print ("3n")
        elif x in fournouns:
            print ("4n")


end = time.time()




print (end - start)