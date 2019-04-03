#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):   # Inspired by Jackson Ho
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Decode digits from binary (base 2)
    # Decode digits from hexadecimal (base 16)
    digits = digits[::-1]
    power = 0
    result = 0
    for i in range(len(digits)):  # range = [0, 1]
        print("Current Character index: {}".format(i))
        power_value = base ** i  # 1
        selected_char = digits[i]  # 0
        character_index = string.hexdigits.find(selected_char) # 0
        product = power_value * character_index
        result += product  # 1 * 0
    return result
    # Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # Encode number in binary (base 2)
    # if base == 2:
    #     binary_str = ''
    #     current_power = 0
    #     power_array = []
    #     finished = False
    #
    #     while finished is False:
    #         bit_value = 2**current_power # initially zero, 1, 2
    #         if bit_value < number: # Current power is less than the number
    #             power_array.insert(0, current_power) # Insert current power to the front of the array
    #             print("Power_array: {}".format(power_array))
    #             current_power += 1
    #             print("Current_power: {}".format(current_power))
    #
    #         elif bit_value == number: # Current power is equal to the number
    #             power_array.insert(0, current_power)
    #             finished = True
    #
    #         else: # The current power is more than the number
    #             finished = True
    #             print("Bit_value: {} is bigger than number: {}".format(bit_value, number))
    #
    #     for power in power_array: # ex: power = 1
    #         value = 2**power # ex: value = 2
    #         if value <= number:
    #             print("Number: {}".format(number))
    #             number -= value
    #             print("Deincremented Number: {}".format(number))
    #             binary_str += "1"
    #
    #         else: # bit_value is greater than number
    #             binary_str += "0"
    #     return binary_str
    # result = '{0:02b}'.format(number)
    # Encode number in hexadecimal (base 16)
    # if base == 16:
    #     hex_str = ""
    #     current_power = 0
    #     list_of_powers = [] # List of all the possible powers but it will be sorted from greatest to largest
    #     finished = False
    #     while finished is False: # Get all the possible power for the number
    #         base_value = 16**current_power
    #         if base_value < number:
    #             list_of_powers.insert(0, current_power)
    #             current_power += 1
    #
    #         elif base_value == number: # Current power is equl to the number
    #             list_of_powers.insert(0, current_power)
    #             finished = True
    #
    #         else: # The current power is more than the number
    #             finished = True
    #
    #     for power in list_of_powers:
    #             current_value = 16**power
    #             limit = int(number/current_value) # How many of one power can go into the number
    #             number -= current_value * limit
    #             hex_str += string.hexdigits[limit]
    #
    #     return hex_str
    # Encode number in any base (2 up to 36)
    encode_str = ''
    current_power = 0
    finished = False
    list_of_powers = []
    while finished is False:  # Get all the possible power of a base for the number
        power_value = base**current_power
        if power_value < number:
            list_of_powers.insert(0, current_power)
            current_power += 1

        elif power_value == number:
            list_of_powers.insert(0, current_power)
            finished = True

        else:  # The current power made the base too big
            finished = True

    for power in list_of_powers:
        power_value = base ** power
        limit = int(number / power_value)
        number -= power_value * limit

        encode_str += string.printable[limit]

    return encode_str


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    # decodes given digits in given base
    print(encode(10, 16))
