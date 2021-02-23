# 3. Write a function cumulative_product() to compute cumulative product of a list of numbers,

print('Please enter as many numbers as you want... enter done when finished')
lists = []                        # Initialize array
while True:
    number = 0
    input_number = input('Please enter a number: ')
    if input_number == 'done':
        break

    try:
        number = int(input_number)
    except ValueError:
        print('Invalid input')
        quit()

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