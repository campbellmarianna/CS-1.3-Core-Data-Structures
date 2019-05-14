"""
Scenario 1: One-time route cost check

You have a carrier route list with 100,000 (100K) entries (in arbitrary order)
and a single phone number. How quickly can you find the cost of calling this number?"""
# Check the book for number and get the price
# Open the file put file info into a list
# Loop through it
# Check if the number makes the given number
# if it does return the set second value
# Else phone number not found

#!python
from pprint import pprint
from hashtable import HashTable

def load_data():
    """
    Returns a list of phone numbers from a file.
    """
    with open('../../project/data/route-costs-4.txt', 'r') as f:
        # f_contents = f.readlines() # list of each line of the file
        # print(f_contents)
        numbers = f.read().split("\n")
    return numbers

def init_hashtable(numbers):
    output_list = []
    ht = HashTable(4)
    for number in numbers: # number gives up +
        combo = number.split(',')
        print(combo)
        num = combo[0]
        price = combo[1]
        ht.set(num, price)
    return ht.items()


if __name__ == '__main__':
    numbers = load_data()
    print(init_hashtable(numbers))
