fobj = open('PE-22-file.txt', 'r')  # I store data in a file
data = sorted(fobj.read().split(','))
fobj.close()
list_name = []
char_index_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                   'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
                   'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                   'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

for i in data:
    i = i.strip('"')
    list_name.append(i)

del data

list_name_index = list(enumerate(list_name, start=1))

del list_name

total = 0

for index, name in list_name_index:
    temp = 0

    for character in name:
        temp += char_index_dict[character]

    total += temp * index

print(total)
