# 5.*  Write  a  function  group(input_list,  length)  that  take  a
# list and splits into smaller lists of given size.
my_list = [1,2,3,4,5,6,7,8,9]
def group(input_list,  length):
    # looping till length l
    for i in range(0, len(input_list), length):
        yield input_list[i:i + length]

        # How many elements each
    # list should have


length = 3

x = list(group(my_list, length))
print(x)