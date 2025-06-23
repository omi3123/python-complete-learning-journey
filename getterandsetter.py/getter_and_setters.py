#without getters and setters
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
emp=Employee("ali",5000)
print(emp.name)
emp.salary=6000
print(emp.salary)
#with getter and setters
class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("invalid salary")
emp=Employee("ali",5000)
print(emp.get_name())
emp.set_salary(6000)
print(emp.get_salary())
#In other way
class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("invalid salary")
emp=Employee("ali",5000)
print(emp.name)
emp.salary=6000
print(emp.salary)
#Rectangle Set and Get
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("Invalid width")
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            print("Invalid height")
    @property
    def area(self):
        return self.__width * self.__height
rect = Rectangle(10, 20)
print(f"Width: {rect.width}, Height: {rect.height}, Area: {rect.area}")
print(f"New Area: {rect.area}")
#Bank Setter and Getter
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
    @property
    def owner(self):
        return self.__owner
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")
account = BankAccount("John Doe", 1000)
print(f"Owner: {account.owner}, Balance: {account.balance}")
account.deposit(500)
print(f"New Balance: {account.balance}")
account.withdraw(300)
print(f"Balance after withdrawal: {account.balance}")
account.withdraw(1500)