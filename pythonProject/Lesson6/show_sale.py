import sys

with open('bakery.csv', 'r', encoding='utf-8') as file:
    i=1
    if len(sys.argv) == 3:
        for line in file:
            if int(sys.argv[2])>=i>=int(sys.argv[1]):
                print(line.strip())
            i+=1
    else:
        for line in file:
            if int(sys.argv[1])<=i:
                print(line.strip())
            i+=1