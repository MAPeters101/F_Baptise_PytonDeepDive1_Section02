i = 0
while i < 5:
    print(i)
    i += 1
i = None
print('='*10)
for i in range(5):
    print(i)
print('='*10)

for i in [1,2,3,4]:
    print(i)

for c in 'hello':
    print(c)

for x in ('a','b','c'):
    print(x)

for x in [(1,2), (3,4), (5,6)]:
    print(x)

for i, j in [(1,2), (3,4), (5,6)]:
    print(i, j)

for i in range(5):
    if i==3:
        continue
    print(i)

for i in range(5):
    if i==3:
        break
    print(i)
print('+'*10)
for i in range(1,5):
    print(i)
    if i%7 == 0:
        print('multiple of 7 found')
        break
else:
    print('No multiples of 7 in the range.')

for i in range(1,8):
    print(i)
    if i%7 == 0:
        print('multiple of 7 found')
        break
else:
    print('No multiples of 7 in the range.')

for i in range(5):
    print('-'*10)
    try:
        10/(i-3)
    except ZeroDivisionError:
        print('Divided by 0')
        continue
    finally:
        print('Always runs.')
    print(i)





