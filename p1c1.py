#  Karatsuba Multiplication

def karatsuba_mul_2(k, j):
    n, m = len(str(k)), len(str(j))
    i = max(n, m)
    if n == m == 1:
        return k*j
    # elif m == 1 or n == 1:
    #     return k*j
    else:
        a, b, c, d = int(k//(10**(i//2))), int(k%(10**(i//2))), int(j//(10**(i//2))), int(j%(10**(i//2)))
        step1, step2 = karatsuba_mul_2(a, c), karatsuba_mul_2(b, d)
        step3 = karatsuba_mul_2(a+b, c+d)
            # what if the digit is n/2 +1 -> n//2
        step4 = step3 - step2 - step1
        return int(step1*10**((i//2)*2) + step4*10**(i//2) + step2)


print(karatsuba_mul_2(3141592653589793238462643383279502884197169399375105820974944592,
                      2718281828459045235360287471352662497757247093699959574966967627))
# RecursionError: maximum recursion depth exceeded while getting the str of an object
# change the data type of a, b, c, d to int

# print(karatsuba_mul_2(543, 12))
