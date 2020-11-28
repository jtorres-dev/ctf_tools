# Future improvements, be able to type a full list of numbers and convert them into a string
# ie input:'1504 1231 1230412 12321'
#   output:'some string'
# Improve formatting
# create a gui
#
#   Change Log( 1.0.0 ):
#            --- Jonathan
#
#               This converter can convert interchangably with any of the choices
#               offered below. The floating point values source code has been provided
#               by geeks for geeks. There are some changes necessary. One change 
#               needed to be changed is to allow the user to input multiple ints 
#               seperated by spaces to get a string value out of it. 
#                
#               This will be an addition added to hex values and binary values as well.
#               As of now, you can enter single values and retrieve a conversion of 
#               your choice. For the floating point values to be converted to a hex, I
#               I wasn't sure if this would be of any help or useful, but I have an 
#               implementation made either way. Same for float to string.
#
#               This version does not have any exceptions being caught. This will come
#               on a later update.
#
#############################################################################################


######################## HELPER FUNCTIONS ############################
#                                                                    #

# returns true if a float, else returns false.
def will_it_float(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False


## function takes in a hexdecimal. 
def hex_to_str(hexval):
    arg_str = ''
    #parses argument as bytes and stores it as a list
    hexval = [hexval[i:i+2] for i in range(0, len(hexval), 2)]

    #convert each byte into a char and concats to arg_str
    for x in range(0, len(hexval)):
        hex_to_int = int(hexval[x], 16)
        arg_str += chr(hex_to_int)
    
    return arg_str

#=========================GEEKS FOR GEEKS============================#
 
# decimal to binary number
# Function returns octal representation 
def float_to_bin(number, places = 3): 
  
    # split() seperates whole number and decimal  
    # part and stores it in two seperate variables 
    whole, dec = str(number).split(".") 
  
    # Convert both whole number and decimal   
    # part from string type to integer type 
    whole = int(whole) 
    dec = int (dec) 
  
    # Convert the whole number part to it's 
    # respective binary form and remove the 
    # "0b" from it. 
    res = bin(whole).lstrip("0b") + "."
  
    # Iterate the number of times, we want 
    # the number of decimal places to be 
    for x in range(places): 
  
        # Multiply the decimal value by 2  
        # and seperate the whole number part 
        # and decimal part 
        whole, dec = str((decimal_converter(dec)) * 2).split(".") 
  
        # Convert the decimal part 
        # to integer again 
        dec = int(dec) 
  
        # Keep adding the integer parts  
        # receive to the result variable 
        res += whole 
  
    return res 
  
# Function converts the value passed as 
# parameter to it's decimal representation 
def decimal_converter(num):  
    while num > 1: 
        num /= 10
    return num  

def IEEE754(arg): 

    # identifying whether the number 
    # is positive or negative 
    sign = 0
    
    if arg < 0: 
        sign = 1
        arg = arg * (-1) 
    
    p = 30
  
    # convert float to binary 
    dec = float_to_bin(arg, places = p) 
  
    # separate the decimal part 
    # and the whole number part 
    whole, dec = str(dec).split(".") 
    whole = int(whole) 
  
    # calculating the exponent(E) 
    exponent = len(str(whole)) - 1
    exponent_bits = 127 + exponent 
  
    # converting the exponent from 
    # decimal to binary 
    exponent_bits = bin(exponent_bits).lstrip("0b") 
  
    # finding the mantissa 
    mantissa = str(whole)[1:exponent + 1] 
    mantissa = mantissa + dec 
    mantissa = mantissa[0:23] 
  
    # the IEEE754 notation in binary 
    final = str(sign) + str(exponent_bits) + mantissa 
  
    # convert the binary to hexadecimal 
    hstr = '%0*X' %((len(final) + 3) // 4, int(final, 2)) 
  
    # return the answer to the driver code 
    return (hstr)
#=========================GEEKS FOR GEEKS============================#


#                                                                    #
######################################################################


##TODO: refine ##
def to_bin(arg):
    
    if arg[0:2] == '0b':
        return arg

    elif arg.isdigit():
        # because the binary value is off by one 0, i have to remove 0b, then add 0b0
        arg = bin(int(arg))[2:]
        arg = '0b' + arg
        return arg

    elif will_it_float(arg):
        return float_to_bin(arg, 7)

    elif arg[0:2] == '0x':
        arg = arg[2:]
        return bin(int(arg, 16))

    # 0b0 misses the leading 0, ord prints the int val of a char, format converts it to a binary, then join concats the 8 bits together with a leading 0.
    # note that unicode contains values with the msb being 1, in this case we dont care about unicode and we are only concerned with ascii.
    elif bool(arg):
        return '0b0' + '0'.join(format(ord(i), 'b') for i in arg)


##TODO: refine##
def to_float(arg):
    
    if arg[0:2] == '0b':
        arg = arg[2:] #will get rid of 0b
        return float(int(arg, 2))
    
    elif arg.isdigit():
        return float(int(arg, 10))

    elif will_it_float(arg):
        return arg

    elif arg[0:2] == '0x':
        binary = to_bin(arg) 
        return float(int(binary, 2))
    
    elif bool(arg):
        arg = arg[2:]
        arg = to_hex(arg).split(' ')
        arg_str = ''
        for x in range(len(arg)):
            arg_str += arg[x]
        return float(int(arg_str, 16))


##TODO: refine##
def to_hex(arg):
    if arg[0:2] == '0b':
        arg = arg[2:] #will get rid of 0b

        arg_in_hex = '0x'

        #converts 00100001 into [0010, 0001]
        arg = [arg[i:i+4] for i in range(0,len(arg), 4)]

        #makes a 4bit into a hex without 0x, then concats to bin_to_hex
        for x in range(0, len(arg)):
            arg_in_hex += hex(int(arg[x], 2))[2:]

        return arg_in_hex

    elif arg.isdigit():
        return hex(int(arg))

    elif will_it_float(arg):
        return float.hex(float(arg))

    elif arg[0:2] == '0x':
        return arg
    
    elif bool(arg):
        return  '0x' + ''.join(format(ord(i), 'x') for i in arg)

##TODO: err thang##
def to_int(arg):
    if arg[0:2] == '0b':
        return int(arg, 2)

    elif arg[0:2] == '0x':
        arg = arg[2:]
        return int(arg, 16)
    
    elif arg.isdigit():
        return arg
    
    elif will_it_float(arg):
        return round(float(arg))
    
    elif bool(arg):
        arg = to_hex(arg).split(' ')    
        arg_str = ''

        for x in range(len(arg)):
            arg_str += arg[x]
        
        return int(arg_str, 16)


##TODO: exceptions, int list condition, optimizations ##
#creates string version of input arg
def to_str(arg):

    if arg[0:2] == '0b': 
        arg = to_hex(arg)[2:]
        return hex_to_str(arg)
    
    elif arg.isdigit():
        arg = to_bin(arg)
        return to_str(arg)

    elif will_it_float(arg):
        return float.hex(float(arg))
    
    elif arg[0:2] == '0x':
        arg = arg[2:]
        return hex_to_str(arg)

    else:
        return arg

   
#########################################################################################################


while True:
    starting_input = input('\nEnter what you would like to convert: ')
    
    print('\nWhat would you like to convert to?')
    print('\n\t1. Binary\n\t2. Boolean\n\t3. Float\n\t4. Hexdecimal\n\t5. Integer\n\t6. ASCII String\n')

    conversion = input('Choose one or type "quit" or "q" to quit: ')
    conversion = conversion.lower()
    
    if conversion == 'q' or conversion == 'quit':
        print('Come back soon!')
        break

    elif conversion == '1' or conversion == 'binary' or conversion == 'bin':
        print(to_bin(starting_input))

    elif conversion == '2' or conversion == 'boolean' or conversion == 'bool':
        print(bool(starting_input))

    elif conversion == '3' or conversion == 'float' or conversion == 'f':
        print(to_float(starting_input))

    elif conversion == '4' or conversion == 'hexdecimal' or conversion == 'hex' or conversion == 'h':
        print(to_hex(starting_input))

    elif conversion == '5' or conversion == 'integer' or conversion == 'int' or conversion == 'i':
        print(to_int(starting_input))

    elif conversion == '6' or conversion == 'ascii' or conversion == 'string' or conversion == 'ascii string' or conversion == 's' or conversion == 'a' or conversion == 'as':
        print(to_str(starting_input))
