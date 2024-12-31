#for loop
num = int(input("Enter the number"));
i = 1 ;
for i in range (1,11):
    print(num,"*",i,"=",num*i);
    i+=1 ;

#while loop
num = 1 ;
while num < 18 :
    print("you are eligible for vote");
    num+=1;

#else with loops
num = int(input("Enter the number"));
i = 1 ;
for i in range (1,11):
    print(num,"*",i,"=",num*i);
    i+=1 ;
else:
    print("table of number is printed");

num = 1 ;
while num < 18 :
    print("you are not eligible for vote");
    num+=1;
else:
    print("you are eligible for vote");

#pass loop
for number in range(1,10):
    if number == 4:
        pass;
    else: 
        print(number);

#break loop
for number in range(1,10):
    if number is 4:
        break;
    else:
        print(number);

#continue loop
for number in range(1,10):
    if number is 4:
        continue;
    else:
        print(number);