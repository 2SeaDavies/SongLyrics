




clean = open('4aClean.txt','w')
with open("4a.txt") as n1, open ("adjectives.txt")as nouns:



    Cleaned = []
    for i in nouns.read().split():
        Cleaned.append(i)

    for x in n1.read().split():
        if x in Cleaned:
            clean.write(x + "\n")





