name = 'Tim'
password = 'chesterpls'

print('Please enter name:')
user = input()
print('Please enter password')
userPassword = input()

if user == name:
    print('Hello Tim')
    if userPassword == password:
        print('Access granted.')
    else:
        print('You shall not pass.')