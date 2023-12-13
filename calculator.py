print('#'*15,'WELCOME TO MY SIMPLE CALCULATOR','#'*15)
first =int(input("Enter First Number: "))
operation=input('ENTER ANY OPERATION YOU WANT TO USE (+,-,*,/,%,**): ')
second=int(input('enter second number: '))
if operation=='+':
    print(first+second)
elif operation=='-':
    print(first-second)
elif operation=='*':
    print(first*second)
elif operation=='/':
    print(first/second)
elif operation=='**':
    print(first**second)
elif operation== '%':
    print(first%second)