# Sort a list
# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
names = ['Claus', 'Ib', 'Per']

# Sort this list by using the sorted() build in function.
sorted_names = sorted(names)
print(sorted_names)

#  Sort the list in reversed order.
sorted_names_reversed = sorted(names, reverse=True)
print(sorted_names_reversed)

# Sort the list on the lenght of the name.
length = sorted(names, key=len)
print(length)

# Sort the list based on the last letter in the name.
sorted_by_last_letter = sorted(names, key=lambda x: x[::-1])
print(sorted_by_last_letter)
# LØSNING CLAUS #


def last(s):
    return s[-1]


sorted_by_last_letter_function = sorted(names, key=last)
print(sorted_by_last_letter_function)

#  Sort the list with the names where the letter ‘a’ is in the name first.


def a_in(s):
    if 'a' in s.lower():
        return True
    return False


sorted_by_a = sorted(names, key=a_in)
print(sorted_by_a)

# 1. Based on this list of tuples: [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

lt = [(1, 2), (2, 2), (3, 2), (2, 1), (2, 2), (1, 5), (10, 4), (10, 1), (3, 1)]


def last_then_first(x):
    return (x[1], x[0])


lt_sorted = sorted(lt, key=last_then_first)
print(f'list not sorted: {lt}')
print(f'list sorted: {lt_sorted}')
