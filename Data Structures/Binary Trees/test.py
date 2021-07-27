name = 'Nilesh'

for i in range(len(name)):
    temp = name[:len(name)-i]
    for j in range(len(temp)):
        print(temp[:len(temp)-j])
    print()