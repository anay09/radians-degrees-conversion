import math


def convert_radians_to_degrees(radian):
    return radian*180/math.pi


def convert_degrees_to_radians(degree):
    return degree*math.pi/180


print('------------Radian and Degrees Conversion------------')
print('Choose one of the following: ')
print('    - A - Convert from Radians to Degrees')
print('    - B - Convert from Degrees to Radians')
print('    - X - Exit\n\n')
option = input("Choose the function : ")
if option == 'A':
    print('You have chosen to convert from radians to degrees...\n')
    radians = int(input('Enter the value to be converted into degrees : '))
    print('\n')
    print(convert_radians_to_degrees(radians))
elif option == 'B':
    print('You have chosen to convert from degrees to radians...\n')
    degrees = int(input('Enter the value to be converted into radians'))
    print('\n')
    print(convert_degrees_to_radians(degrees))
