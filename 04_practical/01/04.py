def sum_tail(n, accumulator=0):
    if n == 0:
        return accumulator
    return sum_tail(n - 1, accumulator + n)

print(sum_tail(5))  
