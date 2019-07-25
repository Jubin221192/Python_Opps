# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:39:45 2019

@author: jubin
"""
# class variable

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        
        self.first = first
        self.last = last
        self.pay = pay
        self.email =last + '.' + first + '@company.com'
        
        Employee.num_of_emps += 1
    
    def fullname(self):
        
        return '{} {}'.format(self.first ,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return 'Pay of {} {} : ${}'.format(self.first ,self.last, self.pay)

emp1 = Employee('Jubin','Mohanty' ,90000)
emp2 = Employee('Snehal','Myndhe' ,95000)
emp1.fullname()

emp1.apply_raise()
emp1.raise_amount

Employee.raise_amount

#if

emp1.raise_amount = 1.05

emp1.apply_raise()
emp1.raise_amount

Employee.num_of_emps



