user_data = input("Enter your binary number, kindly enter '.00' if there are no decimal points: ")
empty_list = list()
for digit in user_data :
    empty_list.append(digit)
dot_index = empty_list.index('.')
pre_dot_number = empty_list[: dot_index]
post_dot_number = empty_list[(dot_index + 1):]
pre_decimal_total = 0
while dot_index >= 0:
    for element in pre_dot_number:
        current_number = ((2**(dot_index))*int(element))
        pre_decimal_total = pre_decimal_total + current_number
        dot_index = dot_index - 1
print(pre_decimal_total)

