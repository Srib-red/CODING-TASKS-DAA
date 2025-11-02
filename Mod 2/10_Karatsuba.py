def karatsuba(x,y):
    if x<10 or y<10:
        return x*y
    temp = x
    x_digit = 0
    while temp != 0:
        temp = temp // 10
        x_digit+=1
    temp = y
    y_digit = 0
    while temp != 0:
        temp = temp // 10
        y_digit+=1
    n = max(x_digit,y_digit)
    m = n//2

    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    a_c = karatsuba(a,c) #(a10M + b)(c10M+d) = ac102M + (ad + bc)10M + bd #(a+b)(c+d)-ac-bd
    b_d = karatsuba(b,d)
    ad_bc = karatsuba(a+b,c+d) - a_c - b_d

    return a_c * (10**(2*m)) + ad_bc * (10**m) + b_d

if __name__ == "__main__":
    print(karatsuba(13254,87563))
