from cmath import phase, polar
import math
def print_coordinates(cord):
    num = complex(cord)
    print(polar(num)[0])
    print((polar(num)[1]))


if __name__ == '__main__':
    cord = 1 + 2j
    print_coordinates(cord)