# 4. Write a function unique() to find all the unique elements of a list.
numbers = [1, 2, 2, 3, 3, 4, 5]


def unique(numbers):

    list_of_unique_numbers = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print(unique(numbers))
# result: [1, 2, 3, 4, 5]