# this covers elif loops 

number = int(input('Enter your number between 0 and 10: '))

def number_range(n):
    if 0 <= n <= 10:
        print('Correct')
    elif n > 10 :
        print('Too High')
    elif n < 0 :
        print('Too Low')


number_range(number)