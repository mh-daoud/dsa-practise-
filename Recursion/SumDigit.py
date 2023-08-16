import math


def sumDigit(number) :
    assert number >= 0 and isinstance(number,int), "please enter a valid positive integer"
    if number <= 9 :
        return number;
        
    reminder = number % 10
    return reminder + sumDigit(math.floor(number / 10));


print(sumDigit(123))