#20230170 ساندي عماد وليم
#20230134 ديمه خالد علام
#20230140روان رشدي فتحي
def menu1():
    print("A) Insert new numbers")
    print("B) Exit")

def menu2():
    print("***pleas select the operation***")
    print("A) Compute one's complement")
    print("B) Compute two's complement")
    print("C) addition")
    print("D) subtraction")

def binary_num1_validation():
    num1 = int(input("please insert a number"))
    intialvalue_num1 = num1
    while num1 > 0:
        j = num1 % 10
        if j != 1 and j != 0:
            print("pleas insert a valid binary number")
            break
        num1 = num1 // 10
        if num1 == 0:
            num1 = intialvalue_num1
            menu2()

def binary_num2_validation():
    num2 = int(input("please insert another number"))
    initialvalue_num2 = num2
    while num2 > 0:
        j = num2 % 10
        if j != 1 and j != 0:
            print("pleas insert a valid binary number")
            break
        num2 = num2 // 10
        if num2 == 0:
           num2 = initialvalue_num2
           print("valid binary number")

def ones_complement(num1):
    num1 = str(num1)
    res = ""
    for x in num1:
        if int(x) == 1:
            res = res + "0"
        elif int(x) == 0:
            res = res + "1"
    print("one's complement of", num1, "is", res)

def twos_complement(num1):
    bin_num = str(num1)
    num = ""
    for i in bin_num:
        if int(i) == 1:
            num = num + "0"
        elif int(i) == 0:
            num = num + "1"
#second add 1 to one's complement
#to add 1 to one's complement they must be the same number of digits
    y = "0"*(len(num)-1) + "1"
#add num1 and num2
    carry = 0
    result = ""
    for digit in range(len(num)-1,-1,-1):
        if int(num[digit]) + int(y[digit]) + carry == 0:
            result = "0" + result
            carry =0
        elif int(num[digit]) + int(y[digit]) + carry == 1:
            result = "1" + result
            carry = 0
        elif int(num[digit]) + int(y[digit]) + carry == 2:
            result = "0" + result
            carry = 1
        elif int(num[digit]) + int(y[digit]) + carry == 3:
            result = "1" + result
            carry = 1
    if carry == 1:
        result = "1" + result
    print("two's complement of" ,num1, "is" ,result)

def bin_addition(num1,num2):
    res = ""
    num1 = str(num1)
    num2 = str(num2)
    num1len = len(num1)
    num2len = len(num2)
    if num1len>num2len:
        i = num1len-num2len
        num2 = "0"*i + str(num2)
    elif num2len>num1len:
        i = num2len - num1len
        num1 = "0"*i + str(num1)
    max_len = num1len
    carry = 0
    for i in range(max_len - 1, -1, -1):
        if int(num1[i]) + int(num2[i]) + carry ==0:
            res = "0" + res
            carry = 0
        elif int(num1[i]) + int(num2[i]) + carry == 1:
            res = "1" + res
            carry = 0
        elif int(num1[i]) + int(num2[i]) + carry == 2:
            res = "0" + res
            carry = 1
        elif int(num1[i]) + int(num2[i]) + carry == 3:
            res = "1" + res
            carry = 1
    if carry == 1:
        res = "1" + res
    print(num1, "+" ,num2, "=" ,res)

def binary_subtraction(num1,num2):
    res = ""
    num1 = str(num1)
    num2 = str(num2)
    num1len = len(num1)
    num2len = len(num2)
    if num1len > num2len:
        i = num1len - num2len
        num2 = "0" * i + str(num2)
    elif num2len > num1len:
        i = num2len - num1len
        num1 = "0" * i + str(num1)
    max_len = num1len
    borrow=0
    for i in range(max_len - 1, -1, -1):
        bit_num1 = int(num1[i])
        bit_num2 = int(num2[i])
        bit_num1 = bit_num1 - borrow
        if bit_num1<bit_num2:
            bit_num1 = bit_num1 + 2
            borrow = 1
        else:
            borrow = 0
        res = str(bit_num1-bit_num2) + res
    print(num1, "-" , num2, "=" ,res)


#problem2
print("***binary calculater***")
while True:
    menu1()
    choice1 = input("please select your choice A/B")
    if choice1 == "A":
        num1 = int(input("please insert a number"))
        intialvalue_num1 = num1
        while num1 > 0:
            j = num1 % 10
            if j != 1 and j != 0:
                print("pleas insert a valid binary number")
                break
            num1 = num1 // 10
            if num1 == 0:
                num1 = intialvalue_num1
                menu2()
                choice2 = input("please select an operation A/B/C/D")
                if choice2 == "A":
                    ones_complement(num1)
                    break
                elif choice2 == "B":
                    twos_complement(num1)
                    break
                elif choice2 == "C":
                    num2 = int(input("please insert another number"))
                    initialvalue_num2 = num2
                    while num2 > 0:
                        j = num2 % 10
                        if j != 1 and j != 0:
                            print("pleas insert a valid binary number")
                            break
                        num2 = num2 // 10
                        if num2 == 0:
                            num2 = initialvalue_num2
                            bin_addition(num1,num2)
                            break
                    break
                elif choice2 == "D":
                    num2 = int(input("please insert another number"))
                    initialvalue_num2 = num2
                    while num2 > 0:
                        j = num2 % 10
                        if j != 1 and j != 0:
                            print("pleas insert a valid binary number")
                            break
                        num2 = num2 // 10
                        if num2 == 0:
                            num2 = initialvalue_num2
                            binary_subtraction(num1,num2)
                            break
                    break
    elif choice1 == "B":
        print("exit problem")
        break
    else:
        print("please enter a valid choice")

