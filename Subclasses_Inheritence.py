# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:57:57 2019

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
    
    
class Developer(Employee):
    
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
    
class Manager(Employee):
    
    def __init__(self, first, last, pay, employee = None):
        super().__init__(first,last, pay)
        
        if employee is None:
            self.employee = []           
        else:
            self.employees = employee

    def add_emp(self, emp):
        if emp not in self.employees:
            self.emplyees.append(emp)
            
    def remove_emp(self,emp):
        
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())
    

print(help(Developer))

o1 = Developer('Jubin','Mohanty', 5000,'Python')

o2 = Developer('Test', 'Employee', 6000,'Java')

print(o1)

mgr_1 = Manager('Sue','Smith',9000,[o1])            

print(mgr_1.email)

mgr_1.add_emp(o1)
mgr_1.remove_emp(o2)
    
mgr_1.print_emp()

print(issubclass(Manager, Employee))


    
    


    
    
    
    
    
    
    
    
        
        