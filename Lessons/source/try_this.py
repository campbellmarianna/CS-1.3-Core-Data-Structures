#encode function psuedocode # Inpsired by Jackson Ho
# create var with string type named encode_str
# create var current_power value with value int 0
# create var finished set to False
# create empty list named list_of_powers
# Run a loop while finished is False
    # multiply the given bass with an exponent of the var set to zero store the product in a var named power_vlue
    # check if power_value is less than the given number
        # if it is insert current_power at index[ ] zero into the list list_of_power
    # okay if that first condition wasn't true check if the power_value is equal to the number
        # if it is insert current_power at index 0
        # set finished to True
    # if none of the first conditions were true
        # set finished to True
    # loop through list_of_powers
        # multiply given bases by power and set that equal to a variable power_value
        # divide given number by power_value and set it to limit make that value stored in limit as a int()
        # deincrement by the product times the limit
        # increment encode_str var by string
