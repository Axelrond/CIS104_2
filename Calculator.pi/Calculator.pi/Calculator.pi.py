import msvcrt
import math
import decimal
import sys

print('''


           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
           _____________________
          |  _________________  |
          | | 0 __________ 0. | |
          | |_________________| |
          |  ___ ___ ___   ___  |
          | | 7 | 8 | 9 | | + | |
         /| |___|___|___| |___| |/
          | | 4 | 5 | 6 | | - | |
          | |___|___|___| |___| |
          | | 1 | 2 | 3 | | x | |
          | |___|___|___| |___| |
          | | . | 0 | = | | / | |
          | |___|___|___| |___| |
          |_____________________|
              oI           Io
\n
\n



Hi, I'm a calculator!\n

Enter an operaiton!\n
+ for addition!\n
- for subtraction!\n
* for multiplication!\n
/ for division!\n
p for power!\n
% for modulo!\n

''')

def calculate(num_str, operator):
    operation = input('''




    number_1 = int(input('Enter the first number! '))
    number_2 = int(input('Enter the second number! '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        float(number_1)
        float(number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == 'p':
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '%':
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Whoops!!! You typed an ivalid operator, please run try again!')\n
''')
    again()

def again():
    calc_again = input('''
print "Do you want to calculate again?
Please type Y for YES or N for NO."
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Bye Bye T_T')
    else:
        again()


