# Dictionaries
 
name = input("Enter the name of the file : ")

file = open(name)

l = []

for line in file:
    if not line.startswith("From:"): 
        continue

    line = line.split()
    l.append(line[1])

count = {}

for word in l:
    count[word] = count.get(word,0) + 1
    #get() method returns the value for the specified key if the key is in the dictionary.

maxcount = None
maxword = None

for word,count in count.items(): 
    if maxcount == None or count > maxcount:
        maxcount = count
        maxword = word

print (maxword,maxcount)