user_data = input("Enter your binary number, kindly enter '.00' if there are no decimal points: ")
empty_list = list()
for digit in user_data :
    empty_list.append(digit)
dot_index = empty_list.index('.')
pre_dot_number = empty_list[: dot_index]
post_dot_number = empty_list[(dot_index + 1):]
pre_dot_index = len(pre_dot_number) - 1
pre_decimal_total = 0 


while pre_dot_index >= 0:

    for element in pre_dot_number:
        current_number = ((2**(pre_dot_index))* int(element))
        pre_decimal_total = pre_decimal_total + current_number
        pre_dot_index = pre_dot_index - 1


post_decimal_index = -1
post_decimal_total = 0
for post_element in post_dot_number:
    current_post_decimal_total = ((2**(post_decimal_index))* int(post_element))
    post_decimal_total = current_post_decimal_total + post_decimal_total
    post_decimal_index = post_decimal_index - 1

total = pre_decimal_total + post_decimal_total
print('Your total is ' + str(total))


