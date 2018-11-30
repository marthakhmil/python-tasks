i=0
while i < 100:
    if i%2==0:print(i,' ',end='')
    i+=1

for i in range(0,100,2):
    print(i,' ',end='')
    
for i in range(0,100):
    if i%2==0:
        continue
    print(i, end=' ')

for i in range(0,100,1):
    print(i,' ',end='')

a=[1,3,7,9,11,13,15]
container=False
for i in a:
    if i%2!=0:
        container=True
        break
if container:
    print('there are only odd numbers')
else:print('there are only enen numbers')
    

a=[1,3,7,9,11,13,15]
i=0
for b in a:
    a[i]=float(b)
    i=i+1
print(a)

