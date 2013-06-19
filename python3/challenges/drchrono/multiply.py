
def  getSingleDigitProduct( n):
    count = 0
    while int(n) > 9:
        mul = 1
        count = count + 1
        number_string = str(n)
        for f in number_string:
            mul = mul * int(f)
        n = mul
    return count





