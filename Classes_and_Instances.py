# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:15:30 2019

@author: jubin
"""

# Classes and Instances

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_1.email
emp_2.fullname()

