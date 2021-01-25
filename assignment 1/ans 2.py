# factorial of a number
num = int(input('enter the num: '))
fact_orial = 1
for x in range(1, num + 1):
    fact_orial = fact_orial * x
print(f'the factorial of {num} is {fact_orial}')
