#Assignment Problem 

# Marks >= 80 - A
# Marks >= 65 - B
# Marks >= 50 - C
# Default - D



marks = int(input('Kindly enter student marks in integer: '))

def get_grade(m):
    if 80 <= m <= 100:
        return 'A'
    elif m > 100 or m < 0:
        return 'Invalid marks'
    elif 65 <= m < 80 :
        return 'B'
    elif 50 <= m < 65 :
        return 'C'
    elif m < 50 :
        return 'D'


print(get_grade(marks))