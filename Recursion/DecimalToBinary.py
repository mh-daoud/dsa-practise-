def decimal2Binary(decimal) :
    if decimal == 0 :
        return ""
    return decimal2Binary(decimal // 2) + str(decimal % 2)

print(decimal2Binary(15))