# 1. What will be the output of the following program?

x = [0, 1, [2]]
x[2][0] = 3
print(x)  # [0, 1, [3]]
x[2].append(4)
print(x)  # [0, 1, [3, 4]]
x[2] = 2
print(x)  # [0, 1, 2]

# 2. What is the output of the following code?
print(type([1, 2]))  # print(type([1,2]))

# 3. What gets printed?
a = [1, 2, 3, None, (), [], ]
print(len(a))  # 6

# 4. What gets printed?
a = {'1': 1, '2': 2, '3': 3, 'None': None}
print(len(a))  # 4

# 5. What gets printed?
name = "snow storm"
print(name[6:8])  # to

# 6. What gets printed?
#name = "snow storm"
#name[5] = 'X'
#print(name)    # TypeError

# 7. What sequence of numbers is printed?
values = [2, 3, 2, 4]


def my_transformation(num):
    return num ** 2


for i in map(my_transformation, values):
    print(i)    # 4, 9, 4, 16

# 8. What gets printed?
foo = (3, 4, 5)
print(type(foo))    # <class 'tuple'>

# 9. What gets printed?
confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)  # 4

# 10. What gets printed?
confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1.0] = 4

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)  # 6

# 11. What gets printed?
boxes = {}
jars = {}
crates = {}

boxes['cereal'] = 1
boxes['candy'] = 2
jars['honey'] = 4
crates['boxes'] = boxes
crates['jars'] = jars

print(len(crates['boxes'])) # 2

# 12. What gets printed?
foo = {1: '1', 2: '2', 3: '3'}
del foo[1]
foo[1] = '10'
del foo[2]
print(len(foo)) # 2

# 13. What gets printed?
names = ['Amir', 'Barry', 'Chales', 'Dao']
print(names[-1][-1])    # o

# 14. What gets printed?
names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)  # 12

# 15. What gets printed?
names1 = ['Amir', 'Barry', 'Chales', 'Dao']

loc = names1.index("Chales")

print(loc)  # 2

# 16. What gets printed?
names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = [name.lower() for name in names1]

print(names2[2][0])     # c

# 17. What gets printed?
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

print(len(list1 + list2))   # 8


# 18. What gets printed?
def addItem(listParam):
    listParam += [1]


mylist = [1, 2, 3, 4]
addItem(mylist)
print(len(mylist))  # 5

# 19. What gets printed?
a = 1
b = 2
a, b = b, a

output = "{} {}".format(a, b)
print(output)   #2 1

# 20. What gets printed?
kvps = {'1': 1, '2': 2}
the_copy = kvps

kvps['1'] = 5

sum_num = kvps['1'] + the_copy['1']
print(sum_num)   # 10

# 21. What gets printed?
kvps = {'1': 1, '2': 2}
theCopy = dict(kvps)

kvps['1'] = 5

sum_num = kvps['1'] + theCopy['1']
print(sum_num)  # 6

# 22. What gets printed?
a, b = 2, 3
c, b = a, c + 1
print(a, b, c)  # NameError






