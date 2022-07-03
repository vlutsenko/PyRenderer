class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@comapny.com"
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    

empl_1 = Employee('John', 'Dough', 5009)

print(empl_1.email)
print(empl_1.fullname())
 
        