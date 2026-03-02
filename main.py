#1-misol
def kvadrat(a):
    return a ** 2

res = kvadrat(5)
print(res)

#2-misol
def koshish(a, b):
    return a + b

res = koshish(3, 3)
print(res)

#4-misol
def juft_yoki_toq(son):
    if son % 2 == 0:
        return "Juft son"
    else:
        return "Toq son"

print(juft_yoki_toq(4))
print(juft_yoki_toq(7))

#5-misol
def tubmi(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(tubmi(5))
print(tubmi(8))
