

def order_007(integers):
    lis = [0, 0, 7]
    x = 0
    for y in integers:

        if y == lis[x]:
            x += 1
        if x >= 3:
            return True

    return False


print(order_007([1, 2, 4, 0, 0, 7, 5]))
print(order_007([1, 0, 2, 4, 0, 5, 7]))
print(order_007([1, 7, 2, 0, 4, 5, 0]))


def list_prime_numbers(count):
    prime_list = [2]

    if count < 2:
        return 0
    for x in range(3, count+1):
        con = True
        for y in range(2, int(x/2)):
            if x % y == 0:
                con = False
                break
        if con:
            prime_list.append(x)
    return prime_list


print(list_prime_numbers(50))


print(format({"x": "string"}))
