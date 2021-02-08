from collections import Counter

f1 = open("words.txt", "r")
wordcount=Counter(f1.readlines())

for k,v in wordcount.items():
    print (k ,v)
