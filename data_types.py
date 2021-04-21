from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
import itertools
from collections import Counter

#1. List manipulation

# a) Create a list with 5 fruit names
fruits = ['apple', 'pear', 'grape', 'orange', 'banana']
fruit_names= fruits

# b) Extend the fruit_names list with 2 vegatables
veg=['potato','tomato']
fruit_names.extend(veg)

# c) Shuffle the list
random.shuffle(fruit_names)

# d) Find the position of first vegetable
first_veg= fruit_names.index(veg[0])
print('The index of potato is', first_veg)

# e) Remove one fruit
fruit_names.remove(random.choice(fruits))

# f) Print the result
print(fruit_names)

# g) Sort the list in alphabetical order
fruit_names=sorted(fruit_names, key=str.lower)
print(fruit_names)

# h) Print each element of a list using a loop
for x in fruit_names:
    print(x)

# i) Modify above code to be able to repeat all above steps
#    to get the same results each time
fruits = ['apple', 'pear', 'grape', 'orange', 'banana']
fruit_names= fruits
veg = ['potato','tomato']
fruit_names.extend(veg)
random.seed(2)
random.shuffle(fruit_names)
first_veg= fruit_names.index(veg[0])
print('The index of potato is', first_veg)
fruit_names.remove(random.Random(500).choice(fruits))
print(fruit_names)
fruit_names=sorted(fruit_names, key=str.lower)
print(fruit_names)
for x in fruit_names:
    print(x)


#2. Tuples

first_list = ["a" + str(number) for number in range(1, 10)]
second_list = ["b" + str(number) for number in range(1, 10)]

# Pair up above lists
paired_list = list(zip(first_list, second_list))
print(paired_list)

# Using a loop unpack the tuple into variables: first_el, secodn_el
# Print the pair position and variables using f-string.
# Example:
# "Index of a3 and b3 is equal 2"
for a, b in paired_list:
    first_el = a
    second_el = b

    print(f'Index of {a} and {b} is equal {first_list.index(a)}')

#3. Sets (unordered & unique data)


fake_names_1 = ['Sherry', 'Mary', 'Matthew', 'Danielle', 'Jeffrey', 'Lauren',
                'Keith', 'Carlos', 'Monique', 'Laura', 'Jared', 'Valerie', 'Juan',
                'Christopher', 'Erica', 'Dawn', 'Joshua', 'Brandon', 'Stephanie']

fake_names_2 = ['Andre', 'Anthony', 'Lauren', 'Douglas', 'Jonathan', 'Richard',
                'Alyssa', 'Vincent', 'Travis', 'Clifford', 'Jerry', 'Justin',
                'Matthew', 'Jared', 'Erica']

# Find the overlapping names in above lists
c = list((Counter(fake_names_1) & Counter(fake_names_2)).elements())
print(c)

# Print number of "duplicated" names
print('Number of "duplicated" names is', len(c))

# Find and print the union of above lists
union_list = list(set().union(fake_names_1, fake_names_2))
print(union_list)

# Find and print the difference between lists
intersection_list = list(set.intersection(set(fake_names_1), set(fake_names_2)))
difference_list = list(set(union_list) - set(intersection_list))
print(difference_list)