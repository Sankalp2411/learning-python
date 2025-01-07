import arthmetic_operator;
class calculator:
    def __init__(self,a,b):
        self.a = a;
        self.b = b;
    def add(self,*args):
        return arthmetic_operator.add(self.a,self.b,*args);
    def sub(self):
        return arthmetic_operator.sub(self.a,self.b);
    def mul(self,*args):
        return arthmetic_operator.mul(self.a,self.b,*args);
    def div(self):
        return arthmetic_operator.div(self.a,self.b);
x = int(input("Enter the first number: "));
y = int(input("Enter the second number: "));
obj = calculator(x,y);
print("Addition: ",obj.add());
print("Subtraction: ",obj.sub());
print("Multiplication: ",obj.mul());
print("Division: ",obj.div());