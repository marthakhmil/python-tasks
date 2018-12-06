print('--------- task 1 ---------')
my_list= [int(x) for x in input('enter 10 numbers:').split()]
print(max(my_list))
print(min(my_list))

print('\n--------- task 2 ---------')
interval=[x for x in range(1,10,1) if x%2==0]
print(interval)
interval_one=[x for x in range(1,10,1) if x%2==1 and x%3==0]
print(interval_one)

print('\n--------- task 3 ---------')
n=int(input('enter n:'))
list_n=list(range(1,n+1,1))
print(list_n)
total=1
if n<=0:
    print('there is no value')
else:
    for i in list_n:
        total*=i
    print('n!=',total)

print('\n--------- task 4 ---------')
login=input('eneter your login:')
while login=='First':
    print('hello, First')
    break
if login!='First':
    print('error, you login - is incorect')

print('\n--------- task 5 ---------')
while True:
    n=int(input('enter some number:'))
    if n<=0:
        print('you number is 0 or negative')
        break
print('\n--------- task 6 ---------')
size=int(input('enter the size of your progression:'))
my_list=[]
while len(my_list)<size:
    number=int(input('enter some number:'))
    if number>0:
        my_list.append(number)
    else:
        print(my_list, 'this is your list, it finished becauce enter some negative number or 0')
        break
    
    

    
   
    
