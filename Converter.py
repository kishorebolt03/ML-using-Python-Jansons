print("---------------------_/\_Welcome_/\_---------------------")

choice='y'
i=1
h=0
while i<100:
    print("            Menu             ")
    print("1.convert binary to decimal \n2.convert decimal to binary \n3.convert decimal to hexadecimal \n4.ceaser cipher\n5.convert decimal to base64\n6.exit")
    n=int(input("Enter your choice"))
    if n==1:
        binary = int(input("Enter binary number ")) 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        print(decimal)

    elif n==2:
        number = int(input("Enter a number to convert into binary: "))

        result = "" 

        while number != 0:
            remainder = number % 2  # gives the exact remainder
            number = number // 2
            result = str(remainder) + result
        print("The binary representation is", result)

    elif n==3:
        hexadecimal=[]
        decimal=int(input("Enter the decimal"))
        quotient = decimal;
 
        while quotient != 0:
            remainder = quotient % 16
            if remainder < 10:
                 hexadecimal.append(chr(48 + remainder))
            else:
                 hexadecimal.append(chr(55 + remainder))
            quotient = quotient // 16

        print(hexadecimal)
    elif n==4:
        text = input("Enter the string to encrypt")
        s = int(input("Enter the key to encrypt"))
        print ("Text  : " + text )
        print ("Shift : " + str(s))
        result = ""
        for i in range(len(text)):
            char = text[i] 
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65) 
  
            else: 
                result += chr((ord(char) + s - 97) % 26 + 97)

        print("Cipher: " + result )
    elif n==5:
        number = int(input("Enter a number to convert into base64: "))

        result = "" 

        while number != 0:
            remainder = number % 64  # gives the exact remainder
            number = number // 64
            result = str(remainder) + result
        print("The base64 representation is", result)
    elif n==6:
        print("Thank you")
        break
    else:
        print("Ivalid input")

    h=int(input("Enter 1 to conitue and 0 to stop"))
    if h==0:
        break
