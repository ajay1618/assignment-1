# sum of  n numbers using while loop
num = int(input('enter the required number:'))
sum = 0
n = 1
while n <= num:
    sum += n
    n += 1
print(f'the sum of n numbers is: {sum}')
