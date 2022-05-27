class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay

    def statement(self):
        return self.first + ' ' + self.last + ' has '+ self.pay + ' rupees.'
        

emp_1 = Employee('Arnav', 'Bhagwat', '5000')

print(emp_1.statement())

