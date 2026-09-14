<<<<<<< HEAD
"""
AI PYTHON EXAM REVIEWER
=======================

Purpose:
A practical, open-notes reviewer for solving one Python problem.
Each section contains short explanations, reusable code patterns,
and comments showing when to use them.

Coverage based on the provided Module 1 and Module 2 reading guides:
environment setup, variables, control flow, data structures, functions,
OOP, inheritance, polymorphism, dunder methods, decorators, recursion,
generators, exceptions, logging, and Git/GitHub workflow.

Tip for the exam:
1. Read the problem carefully.
2. Identify the data, classes, functions, and expected output.
3. Start with a simple working solution.
4. Add validation and error handling.
5. Test normal and invalid cases.
"""


# ============================================================
# 1. ENVIRONMENT SETUP
# ============================================================

# Check Python version in the VS Code terminal:
# py --version
# py -3.12 --version

# Create a Python 3.12 virtual environment:
# py -3.12 -m venv .venv

# Activate on Windows PowerShell:
# .\.venv\Scripts\Activate.ps1

# Install a package:
# pip install package_name

# Check which Python interpreter is being used:
# where.exe python


# ============================================================
# 2. VARIABLES AND BASIC DATA TYPES
# ============================================================

# Python is dynamically typed: no type declaration is required.
student_name = "Francis"       # str
age = 21                       # int
average = 89.5                 # float
is_passed = True               # bool

# Check a value's type:
print(type(student_name))

# A variable can later refer to a different type.
value = 42
value = "forty-two"


# ============================================================
# 3. CONDITIONALS
# ============================================================

# Use if / elif / else to make decisions.

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


# Useful operators:
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal
# <= less than or equal
# and, or, not


# ============================================================
# 4. LOOPS
# ============================================================

# for: use when iterating through a known sequence or range.
for number in range(1, 4):
    print(number)

# while: repeat while a condition is true.
attempts = 0
while attempts < 3:
    attempts += 1
    print(f"Attempt {attempts}")

# break exits a loop early.
# continue skips the current iteration.
for number in range(1, 6):
    if number == 3:
        continue
    if number == 5:
        break
    print(number)


# ============================================================
# 5. DATA STRUCTURES
# ============================================================

# LIST: ordered and mutable.
students = ["Amara", "Leo", "Priya"]
students.append("Sam")
students[0] = "Ana"
print(students[1:])
students.pop()                 # removes and returns the last item
students.remove("Leo")         # removes the first matching value

# Useful list methods:
# append(), insert(), pop(), remove(), index(), sort(), reverse()
# len(list), item in list

# TUPLE: ordered and immutable.
point = (40.7, -74.0)

# DICTIONARY: key-value pairs.
grades = {"Amara": 92, "Leo": 85}
grades["Priya"] = 78
print(grades.get("Unknown", 0))  # safe lookup with a default value

# SET: unique values, no duplicates.
enrolled_ids = {101, 102, 103}
enrolled_ids.add(104)
print(102 in enrolled_ids)


# ============================================================
# 6. COMPREHENSIONS
# ============================================================

# List comprehension: build a list from an iterable.
squares = [x ** 2 for x in range(1, 6)]

# With a condition:
even_numbers = [x for x in range(10) if x % 2 == 0]

# Dictionary comprehension:
square_map = {x: x ** 2 for x in range(1, 6)}


# ============================================================
# 7. FUNCTIONS
# ============================================================

# A parameter is the variable in the function definition.
# An argument is the actual value passed to the function.

def greet(name):
    return f"Hello, {name}!"

message = greet("Amara")
print(message)

# Default parameter:
def calculate_total(price, quantity=1):
    return price * quantity

# Multiple return values are returned as a tuple.
def min_max(numbers):
    return min(numbers), max(numbers)

# *args accepts extra positional arguments.
def add_all(*numbers):
    return sum(numbers)

# **kwargs accepts extra keyword arguments.
def show_info(**info):
    return info


# ============================================================
# 8. OOP: CLASSES, OBJECTS, __init__, AND self
# ============================================================

# A class is a blueprint. An object/instance is created from it.

class Student:
    # Class attribute: shared by the class.
    school = "Example University"

    def __init__(self, name, score=0):
        # Instance attributes: unique to each object.
        self.name = name
        self.score = score

    def display(self):
        return f"{self.name}: {self.score}"

student = Student("Francis", 90)
print(student.display())

# self refers to the particular object calling the method.
# Forgetting self in an instance method causes a TypeError.


# ============================================================
# 9. CLASS ATTRIBUTES AND MUTABLE DATA
# ============================================================

class Counter:
    population = 0

    def __init__(self, name):
        self.name = name
        Counter.population += 1

a = Counter("A")
b = Counter("B")
print(Counter.population)

# Avoid shared mutable class attributes when each object needs its
# own list or dictionary.
class CorrectLogs:
    def __init__(self):
        self.logs = []


# ============================================================
# 10. INHERITANCE AND super()
# ============================================================

class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def status(self):
        return f"{self.name}: {self.battery}% battery"


class CleaningRobot(Robot):
    def __init__(self, name, battery=100, dust_capacity=500):
        # Reuse the parent's initialization.
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity
        self.dust_collected = 0

    def clean(self, amount):
        self.dust_collected = min(
            self.dust_capacity,
            self.dust_collected + amount
        )

cleaner = CleaningRobot("Roomba", dust_capacity=300)
cleaner.clean(50)
print(cleaner.status())


# ============================================================
# 11. METHOD OVERRIDING AND POLYMORPHISM
# ============================================================

class ProtocolRobot(Robot):
    # This replaces the parent's status method.
    def status(self):
        return f"{self.name}: Protocol robot, battery {self.battery}%"

robots = [Robot("R2"), ProtocolRobot("C3")]

# Polymorphism: same method call, different behavior.
for robot in robots:
    print(robot.status())


# ============================================================
# 12. INHERITANCE VS COMPOSITION
# ============================================================

# Inheritance means IS-A:
# CleaningRobot IS-A Robot.

class Battery:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.level = capacity

    def use(self, amount):
        self.level = max(0, self.level - amount)


class ComposedRobot:
    # Composition means HAS-A:
    # A ComposedRobot HAS-A Battery.
    def __init__(self, name):
        self.name = name
        self.battery = Battery()


# ============================================================
# 13. DUCK TYPING, isinstance, AND issubclass
# ============================================================

# Duck typing: if an object has the required method, use it.

class Duck:
    def speak(self):
        return "Quack!"

class AnimalRobot:
    def speak(self):
        return "Beep!"

def make_it_speak(thing):
    return thing.speak()

print(make_it_speak(Duck()))
print(make_it_speak(AnimalRobot()))

# Safe type checks:
# isinstance(object, Class) checks an instance relationship.
# issubclass(Child, Parent) checks a class relationship.


# ============================================================
# 14. MULTI-LEVEL INHERITANCE
# ============================================================

class SmartCleaningRobot(CleaningRobot):
    def __init__(self, name, battery=100, dust_capacity=500):
        super().__init__(name, battery, dust_capacity)
        self.rooms_mapped = []

    def map_room(self, room_name):
        self.rooms_mapped.append(room_name)


# ============================================================
# 15. MULTIPLE INHERITANCE, MIXINS, AND MRO
# ============================================================

class Flyable:
    def fly(self):
        return f"{self.name} takes off!"

class Swimmable:
    def swim(self):
        return f"{self.name} dives in!"

class DroneRobot(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

drone = DroneRobot("Aqua-Drone")
print(drone.fly())
print(drone.swim())

# MRO is Method Resolution Order.
# Python checks the class and its parents in a defined order.
# print(DroneRobot.__mro__)


# ============================================================
# 16. __str__, __repr__, AND __eq__
# ============================================================

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        # Human-readable output for print().
        return f"{self.name}: {self.price:.2f}"

    def __repr__(self):
        # Developer-friendly representation.
        return f"Product(name={self.name!r}, price={self.price!r})"

    def __eq__(self, other):
        # Define equality based on data.
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price


# Other dunder methods to recognize:
# __len__ supports len(object)
# __lt__ supports <
# __add__ supports +


# ============================================================
# 17. INSTANCE, STATIC, AND CLASS METHODS
# ============================================================

class UtilityRobot:
    population = 0

    def __init__(self, name):
        self.name = name
        UtilityRobot.population += 1

    # Instance method: uses self and instance data.
    def greet(self):
        return f"Hello from {self.name}"

    # Static method: related to the class, but needs neither
    # self nor cls.
    @staticmethod
    def is_valid_name(name):
        return bool(name) and name.isalnum()

    # Class method: uses cls and is useful for alternative constructors.
    @classmethod
    def from_config(cls, config):
        return cls(config["name"])


# ============================================================
# 18. @property AND VALIDATION
# ============================================================

class SafeRobot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    @property
    def battery(self):
        # Getter: runs when reading robot.battery.
        return self._battery

    @battery.setter
    def battery(self, value):
        # Setter: runs when assigning robot.battery = value.
        self._battery = max(0, min(100, value))

safe_robot = SafeRobot("R2", 150)
print(safe_robot.battery)  # 100


# ============================================================
# 19. ABSTRACT BASE CLASSES (ABC)
# ============================================================

from abc import ABC, abstractmethod

class AbstractRobot(ABC):
    @abstractmethod
    def perform_task(self):
        # Every child class must implement this method.
        pass

class WorkingRobot(AbstractRobot):
    def perform_task(self):
        return "Task completed"

working_robot = WorkingRobot()
print(working_robot.perform_task())

# AbstractRobot() would raise TypeError because it cannot be
# instantiated until all abstract methods are implemented.


# ============================================================
# 20. HIGHER-ORDER FUNCTIONS AND DECORATORS
# ============================================================

# Functions are first-class values: they can be assigned, passed,
# stored, and returned.

def shout(text):
    return text.upper() + "!"

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(shout, "hi"))


# A decorator adds behavior without changing the original function.

from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@log_call
def welcome(name):
    return f"Welcome, {name}!"

print(welcome("Francis"))

# @log_call is shorthand for:
# welcome = log_call(welcome)

# @wraps preserves the original function's name and metadata.


# ============================================================
# 21. CLOSURES
# ============================================================

# A closure is an inner function that remembers values from its
# enclosing function even after the outer function finishes.

def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))


# ============================================================
# 22. RECURSION
# ============================================================

# A recursive function calls itself.
# It must have a base case to stop.

def factorial(number):
    if number <= 1:             # base case
        return 1
    return number * factorial(number - 1)  # recursive case


# ============================================================
# 23. GENERATORS AND yield
# ============================================================

# A generator produces one value at a time instead of building
# the entire sequence in memory.

def countdown(number):
    while number > 0:
        yield number
        number -= 1

for number in countdown(3):
    print(number)

# next(generator) gets the next value.
# A generator expression uses parentheses:
# squares_generator = (x ** 2 for x in range(1000000))


# ============================================================
# 24. EXCEPTION HANDLING
# ============================================================

# Use try for risky code, except for matching errors,
# else when no error occurs, and finally for cleanup.

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both values must be numbers"
    else:
        return result
    finally:
        print("Division attempt finished")


# Catch specific exceptions instead of using bare except.
# Common exceptions:
# ValueError, TypeError, KeyError, IndexError, AttributeError,
# ZeroDivisionError


# ============================================================
# 25. raise AND CUSTOM EXCEPTIONS
# ============================================================

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw {amount}; balance is only {balance}"
        )

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    print(withdraw(100, 500))
except InsufficientFundsError as error:
    print(f"Transaction failed: {error}")
    print(error.amount)


# ============================================================
# 26. RE-RAISING AND EXCEPTION CHAINING
# ============================================================

def process_number(text):
    try:
        return int(text)
    except ValueError as original_error:
        # Add a clearer error while preserving the original cause.
        raise RuntimeError("Could not process the number") from original_error

# raise by itself inside an except block re-raises the same error.


# ============================================================
# 27. CONTEXT MANAGERS AND with
# ============================================================

# with automatically closes a file even if an error happens.

def save_note(filename, text):
    with open(filename, "w") as file:
        file.write(text)


# ============================================================
# 28. assert
# ============================================================

# assert is for catching programming mistakes during development.
# Do not use it as the main validation for user input.

def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)


# ============================================================
# 29. EAFP VS LBYL
# ============================================================

# LBYL: Look Before You Leap.
def get_value_lbyl(data, key):
    if key in data:
        return data[key]
    return None

# EAFP: Easier to Ask Forgiveness than Permission.
def get_value_eafp(data, key):
    try:
        return data[key]
    except KeyError:
        return None


# ============================================================
# 30. LOGGING
# ============================================================

import logging

logging.basicConfig(level=logging.INFO)

def checked_withdraw(balance, amount):
    if amount > balance:
        logging.error("Withdrawal exceeds the available balance")
        raise ValueError("Insufficient funds")

    new_balance = balance - amount
    logging.info(f"Withdrawal successful; new balance: {new_balance}")
    return new_balance

# Logging levels:
# DEBUG, INFO, WARNING, ERROR, CRITICAL


# ============================================================
# 31. EXAM PROBLEM-SOLVING TEMPLATE
# ============================================================

# Use this structure when the exam asks you to solve a new problem.

class ExampleEntity:
    """Store the data and behavior of one object."""

    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.value}"

    def update(self, amount):
        self.value += amount


def process_entities(entities):
    """Process a collection and return a useful result."""
    results = []

    for entity in entities:
        try:
            entity.update(1)
            results.append(str(entity))
        except (TypeError, ValueError) as error:
            logging.error(f"Could not process entity: {error}")

    return results


# Exam checklist:
# [ ] Identify inputs and expected outputs.
# [ ] Choose list, dict, set, or tuple.
# [ ] Decide whether a class is needed.
# [ ] Add __init__ and self attributes.
# [ ] Add methods for actions.
# [ ] Use inheritance only for a real IS-A relationship.
# [ ] Use super() when extending a parent class.
# [ ] Validate important values.
# [ ] Raise a specific or custom exception when appropriate.
# [ ] Use try/except around operations that can fail.
# [ ] Test normal, boundary, and invalid cases.
# [ ] Keep code readable and avoid unnecessary complexity.


# ============================================================
# 32. GIT AND GITHUB QUICK REFERENCE
# ============================================================

# Git tracks changes and allows you to return to earlier versions.

# Start a repository:
# git init

# Check files and changes:
# git status

# See unstaged changes:
# git diff

# Stage changes:
# git add filename.py
# git add .

# Save a snapshot:
# git commit -m "Add feature"

# View history:
# git log
# git log --oneline
# git log --oneline --graph

# Ignore generated files and secrets in .gitignore:
# __pycache__/
# *.pyc
# .venv/
# .env
# *.log

# Branches:
# git branch
# git switch -c feature-name
# git switch main

# Merge a branch:
# git switch main
# git merge feature-name

# Connect and push to GitHub:
# git remote add origin https://github.com/username/repository.git
# git push -u origin main
# git push

# Download a repository:
# git clone https://github.com/username/repository.git

# Get remote changes:
# git pull

# Temporarily save uncommitted work:
# git stash
# git stash pop

# Undo safely:
# git restore filename.py       # discard uncommitted file changes
# git commit --amend -m "New message"  # fix last unpushed commit
# git revert COMMIT_HASH        # create a new commit that undoes an old one


#.gitignore file
# .venv/


# Avoid git reset --hard on shared history.
# A merge conflict is fixed by editing the marked sections,
# removing <<<<<<<, =======, >>>>>>>, then git add and git commit.

# Tags:
# git tag v1.0.0
# git push origin v1.0.0

# Investigate history:
# git log --author="Name"
# git log -p filename.py
# git blame filename.py
=======
"""
AI PYTHON EXAM REVIEWER
=======================

Purpose:
A practical, open-notes reviewer for solving one Python problem.
Each section contains short explanations, reusable code patterns,
and comments showing when to use them.

Coverage based on the provided Module 1 and Module 2 reading guides:
environment setup, variables, control flow, data structures, functions,
OOP, inheritance, polymorphism, dunder methods, decorators, recursion,
generators, exceptions, logging, and Git/GitHub workflow.

Tip for the exam:
1. Read the problem carefully.
2. Identify the data, classes, functions, and expected output.
3. Start with a simple working solution.
4. Add validation and error handling.
5. Test normal and invalid cases.
"""


# ============================================================
# 1. ENVIRONMENT SETUP
# ============================================================

# Check Python version in the VS Code terminal:
# py --version
# py -3.12 --version

# Create a Python 3.12 virtual environment:
# py -3.12 -m venv .venv

# Activate on Windows PowerShell:
# .\.venv\Scripts\Activate.ps1

# Install a package:
# pip install package_name

# Check which Python interpreter is being used:
# where.exe python


# ============================================================
# 2. VARIABLES AND BASIC DATA TYPES
# ============================================================

# Python is dynamically typed: no type declaration is required.
student_name = "Francis"       # str
age = 21                       # int
average = 89.5                 # float
is_passed = True               # bool

# Check a value's type:
print(type(student_name))

# A variable can later refer to a different type.
value = 42
value = "forty-two"


# ============================================================
# 3. CONDITIONALS
# ============================================================

# Use if / elif / else to make decisions.

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


# Useful operators:
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal
# <= less than or equal
# and, or, not


# ============================================================
# 4. LOOPS
# ============================================================

# for: use when iterating through a known sequence or range.
for number in range(1, 4):
    print(number)

# while: repeat while a condition is true.
attempts = 0
while attempts < 3:
    attempts += 1
    print(f"Attempt {attempts}")

# break exits a loop early.
# continue skips the current iteration.
for number in range(1, 6):
    if number == 3:
        continue
    if number == 5:
        break
    print(number)


# ============================================================
# 5. DATA STRUCTURES
# ============================================================

# LIST: ordered and mutable.
students = ["Amara", "Leo", "Priya"]
students.append("Sam")
students[0] = "Ana"
print(students[1:])
students.pop()                 # removes and returns the last item
students.remove("Leo")         # removes the first matching value

# Useful list methods:
# append(), insert(), pop(), remove(), index(), sort(), reverse()
# len(list), item in list

# TUPLE: ordered and immutable.
point = (40.7, -74.0)

# DICTIONARY: key-value pairs.
grades = {"Amara": 92, "Leo": 85}
grades["Priya"] = 78
print(grades.get("Unknown", 0))  # safe lookup with a default value

# SET: unique values, no duplicates.
enrolled_ids = {101, 102, 103}
enrolled_ids.add(104)
print(102 in enrolled_ids)


# ============================================================
# 6. COMPREHENSIONS
# ============================================================

# List comprehension: build a list from an iterable.
squares = [x ** 2 for x in range(1, 6)]

# With a condition:
even_numbers = [x for x in range(10) if x % 2 == 0]

# Dictionary comprehension:
square_map = {x: x ** 2 for x in range(1, 6)}


# ============================================================
# 7. FUNCTIONS
# ============================================================

# A parameter is the variable in the function definition.
# An argument is the actual value passed to the function.

def greet(name):
    return f"Hello, {name}!"

message = greet("Amara")
print(message)

# Default parameter:
def calculate_total(price, quantity=1):
    return price * quantity

# Multiple return values are returned as a tuple.
def min_max(numbers):
    return min(numbers), max(numbers)

# *args accepts extra positional arguments.
def add_all(*numbers):
    return sum(numbers)

# **kwargs accepts extra keyword arguments.
def show_info(**info):
    return info


# ============================================================
# 8. OOP: CLASSES, OBJECTS, __init__, AND self
# ============================================================

# A class is a blueprint. An object/instance is created from it.

class Student:
    # Class attribute: shared by the class.
    school = "Example University"

    def __init__(self, name, score=0):
        # Instance attributes: unique to each object.
        self.name = name
        self.score = score

    def display(self):
        return f"{self.name}: {self.score}"

student = Student("Francis", 90)
print(student.display())

# self refers to the particular object calling the method.
# Forgetting self in an instance method causes a TypeError.


# ============================================================
# 9. CLASS ATTRIBUTES AND MUTABLE DATA
# ============================================================

class Counter:
    population = 0

    def __init__(self, name):
        self.name = name
        Counter.population += 1

a = Counter("A")
b = Counter("B")
print(Counter.population)

# Avoid shared mutable class attributes when each object needs its
# own list or dictionary.
class CorrectLogs:
    def __init__(self):
        self.logs = []


# ============================================================
# 10. INHERITANCE AND super()
# ============================================================

class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def status(self):
        return f"{self.name}: {self.battery}% battery"


class CleaningRobot(Robot):
    def __init__(self, name, battery=100, dust_capacity=500):
        # Reuse the parent's initialization.
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity
        self.dust_collected = 0

    def clean(self, amount):
        self.dust_collected = min(
            self.dust_capacity,
            self.dust_collected + amount
        )

cleaner = CleaningRobot("Roomba", dust_capacity=300)
cleaner.clean(50)
print(cleaner.status())


# ============================================================
# 11. METHOD OVERRIDING AND POLYMORPHISM
# ============================================================

class ProtocolRobot(Robot):
    # This replaces the parent's status method.
    def status(self):
        return f"{self.name}: Protocol robot, battery {self.battery}%"

robots = [Robot("R2"), ProtocolRobot("C3")]

# Polymorphism: same method call, different behavior.
for robot in robots:
    print(robot.status())


# ============================================================
# 12. INHERITANCE VS COMPOSITION
# ============================================================

# Inheritance means IS-A:
# CleaningRobot IS-A Robot.

class Battery:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.level = capacity

    def use(self, amount):
        self.level = max(0, self.level - amount)


class ComposedRobot:
    # Composition means HAS-A:
    # A ComposedRobot HAS-A Battery.
    def __init__(self, name):
        self.name = name
        self.battery = Battery()


# ============================================================
# 13. DUCK TYPING, isinstance, AND issubclass
# ============================================================

# Duck typing: if an object has the required method, use it.

class Duck:
    def speak(self):
        return "Quack!"

class AnimalRobot:
    def speak(self):
        return "Beep!"

def make_it_speak(thing):
    return thing.speak()

print(make_it_speak(Duck()))
print(make_it_speak(AnimalRobot()))

# Safe type checks:
# isinstance(object, Class) checks an instance relationship.
# issubclass(Child, Parent) checks a class relationship.


# ============================================================
# 14. MULTI-LEVEL INHERITANCE
# ============================================================

class SmartCleaningRobot(CleaningRobot):
    def __init__(self, name, battery=100, dust_capacity=500):
        super().__init__(name, battery, dust_capacity)
        self.rooms_mapped = []

    def map_room(self, room_name):
        self.rooms_mapped.append(room_name)


# ============================================================
# 15. MULTIPLE INHERITANCE, MIXINS, AND MRO
# ============================================================

class Flyable:
    def fly(self):
        return f"{self.name} takes off!"

class Swimmable:
    def swim(self):
        return f"{self.name} dives in!"

class DroneRobot(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

drone = DroneRobot("Aqua-Drone")
print(drone.fly())
print(drone.swim())

# MRO is Method Resolution Order.
# Python checks the class and its parents in a defined order.
# print(DroneRobot.__mro__)


# ============================================================
# 16. __str__, __repr__, AND __eq__
# ============================================================

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        # Human-readable output for print().
        return f"{self.name}: {self.price:.2f}"

    def __repr__(self):
        # Developer-friendly representation.
        return f"Product(name={self.name!r}, price={self.price!r})"

    def __eq__(self, other):
        # Define equality based on data.
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price


# Other dunder methods to recognize:
# __len__ supports len(object)
# __lt__ supports <
# __add__ supports +


# ============================================================
# 17. INSTANCE, STATIC, AND CLASS METHODS
# ============================================================

class UtilityRobot:
    population = 0

    def __init__(self, name):
        self.name = name
        UtilityRobot.population += 1

    # Instance method: uses self and instance data.
    def greet(self):
        return f"Hello from {self.name}"

    # Static method: related to the class, but needs neither
    # self nor cls.
    @staticmethod
    def is_valid_name(name):
        return bool(name) and name.isalnum()

    # Class method: uses cls and is useful for alternative constructors.
    @classmethod
    def from_config(cls, config):
        return cls(config["name"])


# ============================================================
# 18. @property AND VALIDATION
# ============================================================

class SafeRobot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    @property
    def battery(self):
        # Getter: runs when reading robot.battery.
        return self._battery

    @battery.setter
    def battery(self, value):
        # Setter: runs when assigning robot.battery = value.
        self._battery = max(0, min(100, value))

safe_robot = SafeRobot("R2", 150)
print(safe_robot.battery)  # 100


# ============================================================
# 19. ABSTRACT BASE CLASSES (ABC)
# ============================================================

from abc import ABC, abstractmethod

class AbstractRobot(ABC):
    @abstractmethod
    def perform_task(self):
        # Every child class must implement this method.
        pass

class WorkingRobot(AbstractRobot):
    def perform_task(self):
        return "Task completed"

working_robot = WorkingRobot()
print(working_robot.perform_task())

# AbstractRobot() would raise TypeError because it cannot be
# instantiated until all abstract methods are implemented.


# ============================================================
# 20. HIGHER-ORDER FUNCTIONS AND DECORATORS
# ============================================================

# Functions are first-class values: they can be assigned, passed,
# stored, and returned.

def shout(text):
    return text.upper() + "!"

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(shout, "hi"))


# A decorator adds behavior without changing the original function.

from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@log_call
def welcome(name):
    return f"Welcome, {name}!"

print(welcome("Francis"))

# @log_call is shorthand for:
# welcome = log_call(welcome)

# @wraps preserves the original function's name and metadata.


# ============================================================
# 21. CLOSURES
# ============================================================

# A closure is an inner function that remembers values from its
# enclosing function even after the outer function finishes.

def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))


# ============================================================
# 22. RECURSION
# ============================================================

# A recursive function calls itself.
# It must have a base case to stop.

def factorial(number):
    if number <= 1:             # base case
        return 1
    return number * factorial(number - 1)  # recursive case


# ============================================================
# 23. GENERATORS AND yield
# ============================================================

# A generator produces one value at a time instead of building
# the entire sequence in memory.

def countdown(number):
    while number > 0:
        yield number
        number -= 1

for number in countdown(3):
    print(number)

# next(generator) gets the next value.
# A generator expression uses parentheses:
# squares_generator = (x ** 2 for x in range(1000000))


# ============================================================
# 24. EXCEPTION HANDLING
# ============================================================

# Use try for risky code, except for matching errors,
# else when no error occurs, and finally for cleanup.

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both values must be numbers"
    else:
        return result
    finally:
        print("Division attempt finished")


# Catch specific exceptions instead of using bare except.
# Common exceptions:
# ValueError, TypeError, KeyError, IndexError, AttributeError,
# ZeroDivisionError


# ============================================================
# 25. raise AND CUSTOM EXCEPTIONS
# ============================================================

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw {amount}; balance is only {balance}"
        )

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    print(withdraw(100, 500))
except InsufficientFundsError as error:
    print(f"Transaction failed: {error}")
    print(error.amount)


# ============================================================
# 26. RE-RAISING AND EXCEPTION CHAINING
# ============================================================

def process_number(text):
    try:
        return int(text)
    except ValueError as original_error:
        # Add a clearer error while preserving the original cause.
        raise RuntimeError("Could not process the number") from original_error

# raise by itself inside an except block re-raises the same error.


# ============================================================
# 27. CONTEXT MANAGERS AND with
# ============================================================

# with automatically closes a file even if an error happens.

def save_note(filename, text):
    with open(filename, "w") as file:
        file.write(text)


# ============================================================
# 28. assert
# ============================================================

# assert is for catching programming mistakes during development.
# Do not use it as the main validation for user input.

def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)


# ============================================================
# 29. EAFP VS LBYL
# ============================================================

# LBYL: Look Before You Leap.
def get_value_lbyl(data, key):
    if key in data:
        return data[key]
    return None

# EAFP: Easier to Ask Forgiveness than Permission.
def get_value_eafp(data, key):
    try:
        return data[key]
    except KeyError:
        return None


# ============================================================
# 30. LOGGING
# ============================================================

import logging

logging.basicConfig(level=logging.INFO)

def checked_withdraw(balance, amount):
    if amount > balance:
        logging.error("Withdrawal exceeds the available balance")
        raise ValueError("Insufficient funds")

    new_balance = balance - amount
    logging.info(f"Withdrawal successful; new balance: {new_balance}")
    return new_balance

# Logging levels:
# DEBUG, INFO, WARNING, ERROR, CRITICAL


# ============================================================
# 31. EXAM PROBLEM-SOLVING TEMPLATE
# ============================================================

# Use this structure when the exam asks you to solve a new problem.

class ExampleEntity:
    """Store the data and behavior of one object."""

    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.value}"

    def update(self, amount):
        self.value += amount


def process_entities(entities):
    """Process a collection and return a useful result."""
    results = []

    for entity in entities:
        try:
            entity.update(1)
            results.append(str(entity))
        except (TypeError, ValueError) as error:
            logging.error(f"Could not process entity: {error}")

    return results


# Exam checklist:
# [ ] Identify inputs and expected outputs.
# [ ] Choose list, dict, set, or tuple.
# [ ] Decide whether a class is needed.
# [ ] Add __init__ and self attributes.
# [ ] Add methods for actions.
# [ ] Use inheritance only for a real IS-A relationship.
# [ ] Use super() when extending a parent class.
# [ ] Validate important values.
# [ ] Raise a specific or custom exception when appropriate.
# [ ] Use try/except around operations that can fail.
# [ ] Test normal, boundary, and invalid cases.
# [ ] Keep code readable and avoid unnecessary complexity.


# ============================================================
# 32. GIT AND GITHUB QUICK REFERENCE
# ============================================================

# Git tracks changes and allows you to return to earlier versions.

# Start a repository:
# git init

# Check files and changes:
# git status

# See unstaged changes:
# git diff

# Stage changes:
# git add filename.py
# git add .

# Save a snapshot:
# git commit -m "Add feature"

# View history:
# git log
# git log --oneline
# git log --oneline --graph

# Ignore generated files and secrets in .gitignore:
# __pycache__/
# *.pyc
# .venv/
# .env
# *.log

# Branches:
# git branch
# git switch -c feature-name
# git switch main

# Merge a branch:
# git switch main
# git merge feature-name

# Connect and push to GitHub:
# git remote add origin https://github.com/username/repository.git
# git push -u origin main
# git push

# Download a repository:
# git clone https://github.com/username/repository.git

# Get remote changes:
# git pull

# Temporarily save uncommitted work:
# git stash
# git stash pop

# Undo safely:
# git restore filename.py       # discard uncommitted file changes
# git commit --amend -m "New message"  # fix last unpushed commit
# git revert COMMIT_HASH        # create a new commit that undoes an old one


#.gitignore file
# .venv/


# Avoid git reset --hard on shared history.
# A merge conflict is fixed by editing the marked sections,
# removing <<<<<<<, =======, >>>>>>>, then git add and git commit.

# Tags:
# git tag v1.0.0
# git push origin v1.0.0

# Investigate history:
# git log --author="Name"
# git log -p filename.py
# git blame filename.py
>>>>>>> 5d9d7df144b35758ba08b64d4eefbbecf05e51fd
