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






