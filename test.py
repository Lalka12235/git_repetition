print('hello test.py')
a = int(input())
b = int(input())

if a > b:
    print('a > b')
else:
    print('a < b')

print('again/')

from random import randint

random = randint(100,999)
print(random)

for _ in range(0,10):
    if random % 2 == 0:
        print('Odd')
    else:
        print('Even')


from fastapi import FastAPI #delete this row