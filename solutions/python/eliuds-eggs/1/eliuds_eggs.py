def egg_count(display_value):
    # Convert the decimal number into binary (as a string)
    binary_form = bin(display_value)  
    
    # Count how many '1's are in the binary representation
    count_ones = binary_form.count("1")  
    
    # Return that count (the actual number of eggs)
    return count_ones
