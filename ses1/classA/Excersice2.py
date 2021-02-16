# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):

    if len(s) >= 3:
        if s[-3:] == 'ing':
            return f'{s}ly'
        else:
            s[-3:] != 'ing'
            return f'{s}ing'
    else:
        return s

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!


def not_bad(s):
    n = s.find('not')
    b = s.find('bad')
# check if not an bad in string in the right order

   # find not and bad
    n = s.find('not')
    b = s.find('bad')
  # check if not and bad in string and in the right order
    if n < b and n != -1:
        # slice the 'not' ... 'bad' string
        substr = s[n: b+3]
    # replace and return the new string
        return s.replace(substr, 'good', 1)

    return s

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back


def front_back(a, b):
    a_mid = 0
    b_mid = 0
    if len(a) % 2 == 0:
        a_mid = int(len(a)/2)
    else:
        a_mid = int(len(a)/2) + 1

    print(a_mid)
    if len(b) % 2 == 0:
        b_mid = int(len(b)/2)
    else:
        b_mid = int(len(b)/2) + 1

    print(b_mid)
    return a[:a_mid] + b[:b_mid] + a[a_mid:] + b[b_mid:]


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(prefix + ' got: ' + got + ' expected: ' + expected)


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


main()