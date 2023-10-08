def sum_2_num(first,second):
    print(f"Summation of {first}+{second} = {first+second}")

sum_2_num(16,2)


def substraction(first,second):
    return first - second
result=substraction(10,2)
print(f"Substraction : {result}")


def multiplication_4_num(first,second,third,fourth):
    multiply= first*second*third*fourth
    print(f"Multiply : {multiply}")
    return multiply



def division(first,second):
    divide= first/second
    modulus= first % second
    if modulus !=0:
        print(f"Modulus : {modulus}") 
        return divide  
result = division(10,3)
print(result)

