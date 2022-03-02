#basic if, else and elif loops

numerator = float(input('Enter the divisor: '))
denominator = float(input('Enter the dividend: '))

def divide_by (n , d):
    if d == float(0):
        print('Sorry, but your dividend cannot be 0')
    else:
        number = n/d
        return number

print(divide_by(numerator , denominator))