# # Call Routing Project
# *** Pseudocoding solution ideas below, code for scenarios are in scenarios.py***
# Problem - You have a phone number and you want to loop it you have
# Similar to routing in node

"""
Scenario 1: One-time route cost check

You have a carrier route list with 100,000 (100K) entries (in arbitrary order)
and a single phone number. How quickly can you find the cost of calling this number?"""


# Assuming the 100,000 entries are sorted
# Store the single phone number
# Assuming the entries are in a sorted tree
# Conduct Binary Search
# return the the second value of data which is a set

# Assuming the 100,000 entries are put into a hashtable
# Store the single phone number
# Find where the single number is stored in the hashtable and return set second value
# which is the price
# buckets = 10
# Key = phone number
# Value = price
# Conduct Big O Notation

# Keep it simple
# If your boss said I need the price now, what would you do?
# Check the book for number and get the price
# That will work for this first scenario
# The solution you have for sounds good for the second scenario

# Separte the tasks into helper functions
    # Put file data into list
    # See if the prefix is a prefix of a full number from the file

# Check the book for number and get the price
# Open the file put file info into a list
# Loop through it
# Check if the number makes the given number
# if it does return the set second value
# Else phone number not found
