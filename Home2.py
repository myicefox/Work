def sum_digits(number):
    summ = 0
    while number != 0:
        summ += number % 10
        number //= 10
    return summ


arr = [i ** 3 for i in range(1, 1001, 2)]

res1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, arr))
res2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, arr))

print(res1)
print(res2)