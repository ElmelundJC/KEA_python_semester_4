import sys

# Create a list of capital letters in the english alphabet
# Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
# Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

# normalt for-loop
a = []
for x in range(65, 91):
    a.append(chr(x))

print(f'a = {a}')

# list comprehension

b = [chr(x) for x in range(65, 91)]
print(f'b = {b}')


c = [chr(x) for x in range(65, 91) if x not in [70, 75, 80, 85]]
print(f'c = {c}')

print(ord('F'))
print(ord('O'))

# d = []
# for x in range(65, 91):
#    if x in range(70, 79):
#        if x % 2 != 1:
#            d.append(x)
# print(d)

# d = [chr(x) if x in range(70, 79) for x in range(65, 91)]
# print(d)

d = [chr(x) for x in range(65, 91) if x not in range(70, 80, 2)]
print(d)


# From 2 lists, using a list comprehension, create a list containing:

# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

colors_sizes = [(x, y) for x in colors for y in sizes]
print(colors_sizes)

# If the tuple pair is in the following list, it should not be added to the comprehension generated list.

soled_out = [('Black', 'm'), ('White', 's')]

new_list = [item for item in colors_sizes if item not in soled_out]
print(f'new_list = {new_list}')


def main(argv):
    if (sys.argv[1] != 'it'):
        print(
            'For at bruge scriptet skal der skrives: python file.py [-it]{--rm}')

        # def main(argv):
        #    if argv[1] != '-it':
        #        print('Usage: python script.py [-it]{--rm}')
        #    if len(argv) == 3 and argv[2] != '--rm':
        #        print('Usage: python script.py [-it]{--rm}')
        #    elif len(argv) == 3 and argv[2] == '--rm':
        #        print('Goodby')
        #    else:
        #        input()
        #
        #    sys.exit()
        #
        # main(sys.argv)
