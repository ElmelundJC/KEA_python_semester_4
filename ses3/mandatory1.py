print("-------------------------------- 1 ----------------------------------")

directorset = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
managementset = {'Tine', 'Trunte', 'Rane'}
employeeset = {"Niels", "Anna", "Tine", "Ole", "Trunte",
               "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

print(
    f'Direcorset: {directorset} \nManagementset: {managementset} \nEmployeeset: {employeeset}')

print("-------------------------------- 2 ----------------------------------")


# Python code to convert dictionary into list of tuples

dicts = {"a": "Alpha", "b": "Beta", "g": "Gamma"}

# converting into list of tuple

mylist = [(k, v) for k, v in dicts.items()]

# printing list of tuple
print(f'List of tuples: {mylist}')

print("-------------------------------- 3 ----------------------------------")


first_set = {'a', 'e', 'i', 'o', 'u', 'y'}

second_set = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}


print('------ Union --------')
union_set_operator = (first_set | second_set)
union_set_union = first_set.union(second_set)

print(union_set_operator)
print(union_set_union)

print('------ Symetric difference --------')
symetric_difference_set = first_set.symmetric_difference(second_set)

print(symetric_difference_set)
print(first_set ^ second_set)

print('------ Difference --------')
# difference looking at first set
difference_set = first_set - second_set
difference_set_1 = first_set.difference(second_set)
# difference looking at second set
difference_set_2 = second_set.difference(first_set)


print(difference_set)
print(difference_set_1)
print(difference_set_2)

print('------ Disjoint --------')


is_disjoint = first_set.isdisjoint(second_set)
is_disjoint_operator = first_set & second_set

# returns false, which means that the 2 lists has characters in common
print(is_disjoint)
print(is_disjoint_operator)

print("-------------------------------- 4 ----------------------------------")


dictionary_months = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
    'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
    'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

print(dictionary_months)


def translate_month(date):
    date = date.lower().split('-')
    day = date[0]
    month = dictionary_months.get(date[1])
    year = date[2]
    return (('19' + year), month, day)


print(f'Date after decoding: {translate_month("08-MAR-85")}')

# Alternative solution using sys.argv to get user input
# print(translate_month(sys.argv[1]))
