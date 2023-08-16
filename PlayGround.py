def findNumbers( nums):
        evenDigitsCount = 0
        for num in nums :
            digitCount = 0
            if num > 9 :
                singleDigit = num 
                while singleDigit > 9:
                    digitCount = digitCount + 1
                    singleDigit = singleDigit % 10
            if digitCount % 2 == 0 :
                evenDigitsCount = evenDigitsCount + 1
        return evenDigitsCount

    

myList = [12,345,2,6,7896]

print(findNumbers(myList))