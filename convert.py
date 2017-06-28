# convert.py
# Jonathan Munro
# 1/25/2017

''' This program prints the Binary, Decimal, and Hexadecimal notations for a given number. 
The user must provide the number and select the starting notation from console prompts. ''' 


import sys

def bin2dec(string):
    decNum = 0
    count = 0
    for i in range(len(string)-1, -1, -1):
        decNum += (2**count) * int(string[i])
        count += 1
    return str(decNum)

def bin2hex(string):
    #return dec2hex(bin2dec(string))
    hexNum = ""
    if(len(string)%4 !=0):
        string = ("0"*(4-(len(string)%4))) + string
    while(len(string) != 0):
        hexStr = string[-4:]
        string = string[:-4]
        decNum = 0
        count = 0
        for i in range(3, -1, -1):
            decNum += (2**count) * int(hexStr[i])
            count += 1
        if(decNum > 9):
            alist = ['A', 'B', 'C', 'D', 'E', 'F']
            hexNum = alist[decNum - 10] + hexNum
        else:
            hexNum = str(decNum) + hexNum
    return hexNum
            

def dec2bin(string):
    binNum = ""
    intStr = int(string)
    while(intStr != 0):
        binNum = str(intStr%2) + binNum
        intStr = intStr//2
    if(len(binNum)%4 != 0):
        binNum = ("0"*(4-(len(binNum)%4))) + binNum
    return binNum


def dec2hex(string):
    hexNum = ""
    intStr = int(string)
    alphList = ['A', 'B', 'C', 'D', 'E', 'F']
    while(intStr != 0):
        if (intStr%16) <= 9:
            hexNum = str(intStr%16) + hexNum
        else:
            hexNum = alphList[intStr%16 - 10] + hexNum
        intStr = intStr//16
    return hexNum


def hex2bin(string):
    #return dec2bin(hex2dec(string))
    binNum = ""
    count = 0
    for i in range(len(string)-1, -1, -1):
        if string[i] in ['A','B','C','D','E','F']:
            decNum = ord(string[i])-55
        else:
            decNum = int(string[i])
        
        for i in range(4):
            binNum = str(decNum%2) + binNum
            decNum = decNum//2
    return binNum


def hex2dec(string):
    decNum = 0
    count = 0
    for i in range(len(string)-1, -1, -1):
        if string[i] in ['A','B','C','D','E','F']:
            decNum += (16**count) * (ord(string[i])-55)
        else:
            decNum += (16**count) * int(string[i])
        count += 1
    return str(decNum)

def main():
    cont = 'y'
    while cont == 'y':

        num = input("\nnumber (exclude any spaces or '0x'): ")
        data0 = input("number notation (bin/dec/hex): ")
        
        if data0 == "bin":
            print("bin =", num)
            print("dec =", bin2dec(num))
            print("hex =", bin2hex(num))
        elif data0 == "dec":
            print("bin =", dec2bin(num))
            print("dec =", num)
            print("hex =", dec2hex(num))
        elif data0 == "hex":
            print("bin =", hex2bin(num.upper()))
            print("dec =", hex2dec(num.upper()))
            print("hex =", num.upper())
        else:
            print("number type not recognized")
            
        cont = input("again? (y/n) :")
        
main()
