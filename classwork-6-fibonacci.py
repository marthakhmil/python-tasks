n=int(input('enter some number from fibonacci list='))
fibonacci_numbers = [0, 1]
for i in range(2,n):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    if fibonacci_numbers[i]==n:
        break
print('there are some numbers from fibanacci till that you entered',n,'\n',fibonacci_numbers)
