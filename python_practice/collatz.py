def collatz(number):
    try:
        number = int(number)
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(str(number))
            else:
                number = 3 * number + 1
                print(str(number))
    except ValueError:
        print('Aaaagh! That\'s not an integer!')

print('Enter number:')
num = input()
collatz(num)