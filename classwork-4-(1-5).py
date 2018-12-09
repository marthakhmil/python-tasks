print('\n--------task 1----------')
def square_circle(r):
    return (3.14*(r**2))
def square_triangle(a,b,c):
    p=(a+b+c)/2
    print(p)
    square=((p*(p-a)*(p-b)*(p-c))**0.5)
    return square
def square_rectangle(a,b):
    print('the square of rectangle =', a*b)
    return a*b
print('\n 1-rectangle, \n 2-triangle, \n 3-circle')
choice=input('CHOOSE WHAT YOU NEED :')
if choice=='1':
    a=int(input('1 side of rectangle: '))
    b=int(input('2 side of rectangle: '))
    square_rectangle(a,b)
elif choice=='2':
    a=int(input('1 side of triangle: '))
    b=int(input('2 side of triangle: '))
    c=int(input('3 side of triangle: '))
    square_triangle(a,b,c)
elif choice=='3':
    a=int(input('radius of your circle: '))
    square_circle(r)
else: print('you enter option out of range, please try again')   

print('\n--------task 2----------')
def sum_digits(n):
    i=0
    while n!=0:
        i+=n%10
        n//10
    return i

print('\n--------task 3----------')
def multiply_two_number(a,b):
    return a*b
def sum_two_number(a,b):
    return a+b
def subtract_two_number(a,b):
    return a-b
def divide_two_number(a,b):
    return a/b
def degree_of_number(a,b):
    return a**b
def factorial(a):
    num = 1
    while a >= 1:
        num = num * a
        a = a - 1
    return num
def root_number(a):
    return a**0.5
print(' add- 1,\n subtract-2,\n multiply-3,\n divide-4,\n degree of number-5,\n X!-6,\n root number-7,\n EXIT - 8')
i=1
while i==1:
    your_choice=input('choose an action:')
    if  your_choice=='1':
        a=float(input('enter frist number:'))
        print('+')
        b=float(input('enter second number:'))
        print(a,'+',b,'=', sum_two_number(a,b))
    elif your_choice=='2':
        a=float(input('enter frist number:'))
        print('-')
        b=float(input('enter second number:'))
        print(a,'-',b,'=', subtract_two_number(a,b))
    elif your_choice=='3':
        a=float(input('enter frist number:'))
        print('x')
        b=float(input('enter second number:'))
        print(a,'x',b,'=', multiply_two_number(a,b))
    elif your_choice=='4':
        a=float(input('enter frist number:'))
        print('/')
        b=float(input('enter second number:'))
        print(a,'x',b,'=', divide_two_number(a,b))
    elif your_choice=='5':
        a=float(input('enter frist number:'))
        print('**')
        b=float(input('enter second number:'))
        print(a,'^',b,'=', degree_of_number(a,b))
    elif your_choice=='6':
        a=int(input('enter number:'))
        print(a,'!=', factorial(a))
    elif your_choice=='7':
        a=int(input('enter number:'))
        print(a,'^0.5=', root_number(a))
    elif your_choice=='8':
        print('thanks that you used my app')
        break

print('\n--------task 4----------')
def fibonacci(n):
    fibonacci_numbers = [0, 1]
    for i in range(2,n):
         return fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
        if fibonacci_numbers[i]==n:
            break
    print('there are some numbers from fibanacci till that you entered',n,'\n',fibonacci_numbers)
            

print('\n--------task 5----------')
def discriminant():
    a=int(input('enter a='))
    b=int(input('enter b='))
    c=int(input('enter c='))
    print(a,'x**2 +',b,'x +',c,'=0')
    print('D=b^2–4ac')
    return (b**2)+(4*a*c)
    
