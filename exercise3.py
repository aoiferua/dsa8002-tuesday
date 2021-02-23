# 3. Write a function cumulative_product() to compute cumulative product of a list of numbers,

lists = []                        # Initialize array
for i in range(5):

    input_number = input('Please enter a number: ')
    try:
        number = int(input_number)
    except ValueError:
        print('Invalid input')
        continue

    lists.append(int(input_number))


def cumulative_product(lists):
    cu_list = []
    cur = 1
    for n in lists:
        cur *= int(n)
        cu_list.append(cur)
    return cu_list


print(lists)
print(cumulative_product(lists))