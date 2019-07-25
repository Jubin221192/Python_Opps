# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 19:14:38 2019

@author: jubin
"""

class Employee:
    
    no_of_emp = 0
    raise_pay = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
        Employee.no_of_emp += 1
        
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_pay)
        
        return self.pay
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_pay = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or day.weekday() == 6:
            return False
        return True
    
e1 = Employee('Jubin', 'Mohanty', 5000)
e2 = Employee('Rahim', 'Saini', 6000)

e1.fullname()
e2.apply_raise()

Employee.raise_pay

Employee.set_raise_amt(1.5)

emp_1 ='Snehal-Mundhe-9000'

xyz = Employee.from_string(emp_1)
print(xyz.email)

e1.email

import datetime

my_date = datetime.date(2019, 7, 24)

print(Employee.is_workday(my_date))








