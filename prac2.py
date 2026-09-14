#Scenario: A company has different types of employees. Every employee has a name and base_salary.
#There are three employee types:
#Developer: Gets a 20% bonus.
#Manager: Gets a 30% bonus.
#Intern: Does not get a bonus.
#Task:
#Create an abstract base class Employee using abc.ABC.
#Add an abstract method calculate_salary() to the Employee class.
#Implement the calculate_salary() method in the Developer, Manager, and Intern classes.
#Create a function total_payroll() that takes a list of Employee objects and returns the total payroll amount.
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
   
    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        return self.base_salary * 1.2  # Developers get a 20% bonus
    
class Manager(Employee):
    def calculate_salary(self):
        return self.base_salary * 1.3  # Managers get a 30% bonus
    
class Intern(Employee):
    def calculate_salary(self):
        return self.base_salary # Interns do not get a bonus

 #polymorphism example   
def total_payroll(employees: list [Employee]) -> float:
    total = 0
    for employee in employees:
        total += employee.calculate_salary()
    return total

developer = Developer("Alice", 50000)
manager = Manager("Bob", 60000) 
intern = Intern("Charlie", 40000)

print(f"{developer.name}'s salary: {developer.calculate_salary()}")
print(f"{manager.name}'s salary: {manager.calculate_salary()}") 
print(f"{intern.name}'s salary: {intern.calculate_salary()}")

employees = [developer, manager, intern]
print(f"Total payroll: {total_payroll(employees)}")

#absract class test

try:
    employees = Employee("David", 70000)  # This should raise an error because Employee is abstract
except TypeError as e:
    print("Cannot create employee directly:")
    print(e)


    
