print("This is comparison code to find biggest or smallest number from given numbers.\n")
choice = str(input("What you want?\nBiggest number or Smallest number.\n"))
if choice == "Biggest":
    count = int(input("How much numbers did you have?\n"))
    num1 = int(input("enter the first number\n"))
    i=1
    while i in range(1,count):
        num2 = int(input("enter the next number\n"))
        if num1<num2:
            num1 = num2
        i=i+1
    print(num1)

elif choice == "Smallest":
    count = int(input("How much numbers did you have?\n"))
    num1 = int(input("enter the first number\n"))
    i=1
    while i in range(1,count):
        num2 = int(input("enter the next number\n"))
        if num1>num2:
            num1 = num2
        i=i+1
    print(num1)
else:
    print("wrong choice\nplease check you enter 'Biggest'or'Smallest'")