




clean = open('4vClean.txt','w')
with open("4v.txt") as n1, open ("verbs.txt")as nouns:



    Cleaned = []
    for i in nouns.read().split():
        Cleaned.append(i)

    for x in n1.read().split():
        if x in Cleaned:
            clean.write(x + "\n")





