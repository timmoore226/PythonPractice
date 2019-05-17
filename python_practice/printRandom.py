import random
matches = 0
top = 5000
for i in range(top):
    number = random.randint(1, top)
    match = i == number
    string = str(i) + ' : ' + str(number)
    if match:
        matches = matches + 1
        string = string + ' - match!'
    print(string)
print()
prob = 100 / top
actual = matches / top * 100
print('Number of matching pairs: ' + str(matches))
print('Probability: ' + str(prob) + '%')
print('Actual: ' + str(actual) + '%')