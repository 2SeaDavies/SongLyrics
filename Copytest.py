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
# Import time and open the files
import time
MyFile=open('Wooden.txt','r')
words={}
count=0
songout = open('copytest.txt','w')



start = time.time()


#testing replacing words
for x in MyFile.readlines():
    for word in x:
        if word == "me":
            word.replace('me', 'something')



MyFile=open('Wooden.txt','r')
#printing the edited song
for x in MyFile.readlines():
    print(x)
    songout.write(x)

end = time.time()

print (end - start)