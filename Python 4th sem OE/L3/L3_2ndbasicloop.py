#basic if, else and elif loops



number = int(input('Enter a number between 0 and 10: '))

def easy_method(n):
    if 0 <= n <= 10:     
        print('Correct')
    else: 
        print('Error')

easy_method(number)