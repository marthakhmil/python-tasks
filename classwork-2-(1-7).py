print('\n-------- task 1-----------')
i=0                                 
while i < 100:
    if i%2==0:print(i,' ',end='')
    i+=1

for i in range(0,100,2):
    print(i,' ',end='')
    
print('\n-------- task 2-----------')    
for i in range(0,100):
    if i%2==0:
        continue
    print(i, end=' ')

for i in range(0,100,1):
    print(i,' ',end='')

print('\n-------- task 3-----------')
a=[1,3,7,9,11,13,15]
container=False
for i in a:
    if i%2!=0:
        container=True
        break
if container:
    print('there are only odd numbers')
else:print('there are only enen numbers')
    
print('\n-------- task 4-----------')
a=[1,3,7,9,11,13,15]
i=0
for b in a:
    a[i]=float(b)
    i=i+1
print(a)
print('\n-------- task 5-----------')
n=int(input('enter some number from fibonacci list='))
fibonacci_numbers = [0, 1]
for i in range(2,n):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    if fibonacci_numbers[i]==n:
        break
print('there are some numbers from fibanacci till that you entered',n,'\n',fibonacci_numbers)

print('\n-------- task 6-----------')
list_str=['dodo','roro','momo','soso']
for i in list_str:
    print(i)

print('\n-------- task 7-----------')
list_str=['dodo','roro','momo','soso']
for i in list_str:
    print(i+"", end="#")


