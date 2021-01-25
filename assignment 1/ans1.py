# program to print all prime numbers in an interval
lower = int(input('lower limit of the interval: '))
upper = int(input('upper limit of the interval: '))
print(f'the prime numbers between {lower} and {upper} are :')
for num in range(lower, upper + 1):
    for divisor in range(2, num):
        if num % divisor == 0:
            break
    else:
        print(num)

