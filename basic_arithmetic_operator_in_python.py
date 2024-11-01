def add(a,b):
    c = a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mult(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
first_number= int(input("enter first number\n"))
second_number=int(input("enter second name\n")) 
print("what is operator\n+ for addition\n- for substraction\n* for multiplication\n/ for division")
operator = input("enter operator\n")
if operator == "+" :
    ans = add(first_number,second_number)
elif operator == "-":
    ans = sub(first_number,second_number)
elif operator == "*":
    ans = mult(first_number,second_number)
elif operator == "/":
    ans = div(first_number,second_number)
else :
    ans = "wrong choice"
print(first_number,operator,second_number,"=",ans)