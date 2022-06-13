# Files

name = input("Enter the file name : ")

file = open(name)

count = 0
sum = 0

for i in file:
    if not i.startswith("X-DSPAM-Confidence:"):
        continue
    t = i.find("0")
    num = i[t:]
    number = float(num)
    sum=sum + number
    count = count + 1

avg = sum/count
print("Average spam confidence:",avg)
