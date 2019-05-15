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
    Returns a list of phone numbers and prices from a file.
    """
    route_costs = []
    with open('../../project/data/route-costs-4.txt', 'r') as f:
        for line in f:
            prefix, price = line.split(',')
            route_costs.append((prefix, price))
    return route_costs

def init_hashtable(route_costs, phone_num):
    """
    Add phone number (key) and price (value) in the hashtable and return
    hashtable items to proven the data is inserted correctly.
    """
    output_list = []
    num_buckets = len(route_costs)
    ht = HashTable(num_buckets)
    for prefix, price in route_costs: # number gives up +
        print("Phone number and price:", prefix, price)
        ht.set(prefix, price)
    print("Phone Number:", phone_num)
    # Check if have a prefix that matches the start of a phone_num
    if ht.contains(phone_num):
        return print("Route Cost for {}: ${}".format(phone_num, ht.get(phone_num)))
    else:
        raise ValueError("Phone number not found.")

def is_prefix_match_and_get_price(phone_num):
    """
    Return True if the prefix we have on record is the start of a phone we give
    as input otherwise return False
    """
    # you've got a phone do we have a prefix that matches it
    # contains
    # get the price

    if self.contains(phone_num):
        self.get()


if __name__ == '__main__':
    route_costs = load_data()
    print("Phone Numbers and Prices:", route_costs)
    print("***")
    print(init_hashtable(route_costs, '+15124156620'))
