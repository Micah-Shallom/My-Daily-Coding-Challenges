# using map and filter functions

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

print(list(zip(my_strings,my_numbers)))
print(list(map(lambda x,y : (x,y) , my_strings , my_numbers)))

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def filters(scores):
    return scores > 70

print(list(filter(filters, scores)))

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

print(list(filter(lambda word: word == word[::-1], dromes)))

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

print(reduce(lambda x , y: x + y , numbers, 0))


# def listComp(x,y,z,n):
#     pass

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     print(listComp(x,y,z,n))