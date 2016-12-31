print [(5.0/9.0 * (x - 32), x) for x in range(-40, 120, 10) if x not in (0, 50)]

print {(5.0/9.0 * (x - 32), x) for x in range(-40, 120, 10) if x not in (0, 50)}

my_dict = {x: 5.0/9.0 * (x - 32) for x in range(-40, 120, 10) if x not in (0, 50)}

print my_dict

"""
This program reads a temperature in fahrenheit from
the keyboard, converts it to centigrade (in a function) and prints the
results. Then it requests another input from the keyboard.
"""
# def fahrenheit_to_centigrade(xtmp):
#     nutmp = 5.0 / 9.0 * (xtmp - 32)
#     return nutmp  # or combine the two in a return statement as below:
#                   # return 5./9.*(xtmp-32)

while True:
    temp = input('Enter a temperature: ')
    if temp == 'q' or temp == 'Q':
        break
    try:
        ftemp = float(temp)
    except ValueError:
        print('Input contains non-numeric data - try again')
        continue
    f_to_c = lambda xtmp: int(5.0 / 9.0 * (xtmp - 32))
    ctemp = f_to_c(ftemp)
    print('{:.1f} degrees Fahrenheit is {:.1f} degrees Centigrade'.format(
        ftemp, ctemp))
