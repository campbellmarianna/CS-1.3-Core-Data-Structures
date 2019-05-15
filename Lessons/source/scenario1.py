'''Scenario 1: One-time route cost check
You have a carrier route list with 100,000 (100K) entries (in arbitrary order)
and a single phone number. How quickly can you find the cost of calling this number?'''
# Check the book for number and get the price
# Open the file put file info into a list
# Loop through it
# Check if the number makes the given number
# if it does return the set second value
# Else phone number not found
# 4 minutes first time
#!python
import time

from pprint import pprint
from hashtable import HashTable
# import glob
import os

def load_data():
    """
    Returns a list of phone prefixes and prices from a file.
    """
    # all_route_costs = glob.glob(os.path.join('', 'route-costs-*.txt'))
    route_costs = []
    # for route in all_route_costs:
        # with open(route, 'r') as f:
    with open('route-costs-10000000.txt', 'r') as f:
        for line in f:
            prefix, price = line.split(',')
            pprice = price.replace("\n", "")
            route_costs.append((prefix, pprice))
    return route_costs
    # put file names in a list
    # loop through each file
        # open each file

def init_hashtable(route_costs):
    """
    Add phone number (key) and price (value) in the hashtable and return
    hashtable items to proven the data is inserted correctly.
    """
    output_list = []
    num_buckets = len(route_costs)
    ht = HashTable(num_buckets)
    for prefix, price in route_costs: # number gives up +
        # print("Phone number and price:", prefix, price)
        ht.set(prefix, price)

    # Check if have a prefix that matches the start of a phone_num

    return ht



def is_prefix_match_and_get_price(ht, phone_num):
    """
    Return True if the prefix we have on record is the start of a phone we give
    as input otherwise return False
    """
    # print("Phone Number:", phone_num)
    # base case
    if not phone_num:
        return 0

    #check if the phone number is in the HashTable
    if ht.contains(phone_num):
        # print("What we get:", ht.get(phone_num))
        # if yes, return the price
        return ht.get(phone_num)
    #if not, pop off the last digit of the phone number
    else:
        phone_num = phone_num[:-1]
        return is_prefix_match_and_get_price(ht, phone_num)

def get_prices(phone_numbers, is_prefix_match_and_get_price, ht):
    #create prices list
    price_list = []

    #loop through the phone numbers
    for number in phone_numbers:
        #pass one phone number into the prefix match function
        # append price to the list
        price = is_prefix_match_and_get_price(ht, number)
        price_list.append((number, price))

    return price_list

def load_phone_nums():
    """
    Returns a list of phone numbers.
    """
    phone_numbers = []

    with open('../../project/data/phone-numbers-10000.txt', 'r') as f:
        for line in f:
            # print(line)
            individual_phone_num = line.replace("\n", "")
            phone_numbers.append(individual_phone_num)

    return phone_numbers


if __name__ == '__main__':
    start = time.time()
    route_costs = load_data()
    # print("Phone Numbers and Prices:", route_costs)
    # print("***")
    ht = init_hashtable(route_costs)
    phone_numbers = load_phone_nums()
    price_list = get_prices(phone_numbers, is_prefix_match_and_get_price, ht)
    print(price_list)
    # print(is_prefix_match_and_get_price(ht, phone_numbers))
    # print(load_phone_nums())
    end = time.time()
    print(end - start)
