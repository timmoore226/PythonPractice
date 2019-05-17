catNames = []

while True:
    print('Enter the name for cat #' + str((len(catNames) + 1)) + ' (or just hit enter to exit):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are:')
for i in range(len(catNames)):
    print(str(i + 1) + ' - ' + catNames[i])