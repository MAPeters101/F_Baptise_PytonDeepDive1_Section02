l = [
    1, #item 1
    2, #item 2
    3, #item 3
]
print(l)

l = [
    i**2
    for i in range(100)
    if i%2
]
print(l)

a = (
    10 +
    20
)
print(a)

def my_func(a,
            b, # comment
            c):
    pass

a = b = c = 1
if a \
    and b \
    and c:
    pass

# if a \
#     and b \  # comment
#     and c:
#

a = '''this is
a multi-line string'''
print(a)

a = [1, 2, 3]
print(a)

a = [1, 2,
     3, 4, 5]
print(a)

a = [1, # comment
     2]
print(a)

# a = [1 # comment,
#      2]
# print(a)

a = [1 # comment
     ,2]
print(a)


a = (1 #comment
    ,2 #comment
    ,3)
print(a)

a = {'key1': 1 #comment
    ,'key2': 2 #comment
    }
# a = {'key1': 1 #comment
#     ,'key2': 2 #comment }
print(a)

def my_func(a, #comment
            b, #comment
            c):
    print(a, b, c)

my_func(10, 20, 30)
my_func(10, #comment
        20, #comment
        30 #comment
        )

a = 10
b = 20
c = 30

if a > 5 and b > 10 and c > 20:
    print('yes')

if a > 5 \
   and b > 10 \
   and c > 20:
    print('yes')

a = '''this is a string'''
print(a)

a = '''this
 is a string'''
print(a)

a = '''this
    is a string
        that is created over multiple lines'''
print(a)

a = '''some items:
        1. item 1
        2. item 2'''
print(a)


def my_func():
    a = '''a multi-line string
    that is indented in the second line'''
    return a

print(my_func())

def my_func():
    a = '''a multi-line string
that is indented in the second line'''
    return a

print(my_func())





