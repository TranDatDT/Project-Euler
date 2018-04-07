fobj = open('PE-13-file.txt')  # I store the number in a file
li = fobj.readlines()
fobj.close()

total = 0

for i in li:
    i = i.strip('\n')
    total += int(i)

del li

print(str(total)[:10])
