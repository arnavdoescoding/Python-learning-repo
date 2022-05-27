class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay

    def statement(self):
        return self.first + ' ' + self.last + ' has '+ self.pay + ' rupees.'
    
    @classmethod  
    def set_raise(cls, amount):
        cls.raise_amt = amount

emp_1 = Employee('Arnav', 'Bhagwat', '5000')

