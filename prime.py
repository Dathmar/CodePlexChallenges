# check if number is prime
from math import floor

def is_prime(num):
    if num % 2 == 0:
        return False

    for i in range(3, floor(num/2)):
        if num % i == 0:
            return False

    return True


num = int(input('gimme dat number: '))

print(str(num) + ' is prime? ' + str(is_prime(num)))

