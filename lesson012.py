a = 10
b = 0
try:
    a/b
except ZeroDivisionError:
    print('Division by 0')
finally:
    print('This always executes')



a = 0
b = 2
while a < 4:
    print('-'*10)
    a += 1
    b -= 1
    try:
        a/b
    except ZeroDivisionError:
        print('{0}, {1} - Division by 0'.format(a, b))
        continue
    finally:
        print('{0}, {1} - This always executes'.format(a, b))

    print('{0}, {1} - Main loop'.format(a, b))

