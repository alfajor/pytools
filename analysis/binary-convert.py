def binary_to_string(bin_str):
    num = int(bin_str, 2)
    conversion = num.to_bytes((num.bit_length() + 7) // 8, 'big').decode()
    
    print(conversion)

binary_to_string('01110000011110010111010001101000011011110110111000100000011100110111010001110010011010010110111001100111')