




clean = open('1nClean.txt','w')
with open("1n.txt") as n1, open ("nouns.txt")as nouns:



    Cleaned = []
    for i in nouns.read().split():
        Cleaned.append(i)
        print (i)

    for x in n1.read().split():
        if x in Cleaned:
            clean.write(x + "\n")
            print (x)




