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
# open files
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

#create sets of words from files
with open("1n.txt") as n1,open("2n.txt") as n2,open("3n.txt") as n3,open("4n.txt") as n4,open("1a.txt") as a1,open("2a.txt") as a2,open("3a.txt") as a3,open("4a.txt") as a4,open("1v.txt") as v1,open("2v.txt") as v2,open("3v.txt") as v3,open("4v.txt") as v4,open("Wooden.txt") as f2:
    onenouns=set(line.strip() for line in n1)
    twonouns = set(line.strip() for line in n2)
    threenouns = set(line.strip() for line in n3)
    fournouns = set(line.strip() for line in n4)
    oneadj = set(line.strip() for line in a1)
    twoadj = set(line.strip() for line in a2)
    threeadj = set(line.strip() for line in a3)
    fouradj = set(line.strip() for line in a4)
    oneverb = set(line.strip() for line in v1)
    twoverb = set(line.strip() for line in v2)
    threeverb = set(line.strip() for line in v3)
    fourverb = set(line.strip() for line in v4)



    for x in f2.read().split():
         #if the word is found, print the character
        if x in onenouns:
            Templates.write("1n")
        elif x in twonouns:
            Templates.write("2n")
        elif x in threenouns:
            Templates.write("3n")
        elif x in fournouns:
            Templates.write("4n")
        elif x in oneadj:
            Templates.write("1a")
        elif x in twoadj:
            Templates.write("2a")
        elif x in threeadj:
            Templates.write("3a")
        elif x in fouradj:
            Templates.write("4a")
        elif x in oneverb:
            Templates.write("1v")
        elif x in twoverb:
            Templates.write("2v")
        elif x in threeverb:
            Templates.write("3v")
        elif x in fourverb:
            Templates.write("4v")
        else:
            Templates.write(x)



end = time.time()




print (end - start)