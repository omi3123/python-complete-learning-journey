#Bank Account
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_ = acc
    def debit(self, amount):
        self.balance -= amount
        print("Amount is debited")
        print("Total balance is: ", self.balanceee())
    def credit(self, amount):
        self.balance += amount
        print("Amount is credited")
        print("Total balance is: ", self.balanceee())
    def balanceee(self):
        return self.balance
acc1 = Account(10000, 25000)
acc1.debit(5000)
acc1.credit(3000)
#Shapes
class Rectangle:
    def area(self,width,length):
        return length*width
class Circle:
    def area(self,radius):
        return 2*3.14*radius
def Area(shape):
    if isinstance(shape,Rectangle):
        print(f"Area of Rectangle is: {shape.area(4,5)}")
    elif isinstance(shape,Circle):
        print(f"Area of Circle is: {shape.area(3)}")
rect=Rectangle()
circ=Circle()
Area(rect)
Area(circ)