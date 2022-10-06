""" https://www.youtube.com/watch?v=7MT7bZWJ3Uk&list=PL-tKrPVkKKE1Y_o_h2w85dzVdoX5t7SI0&index=9
    With jadi's help :)
 """


def is_prime(num):
    prime = True
    range_num = (num ** 0.5) + 1
    for i in range(2, int(range_num)):
        if (num % i == 0):
            prime = False
            break
    return prime


def numbers(my_range):
    last_prime = 0
    count = 0
    for j in range(1, my_range):
        if is_prime(j):
            last_prime = j
            count += 1
    else:
        print(f"last prime number is {last_prime}")
        print(f"There are {count} prime numbers in the range.")


numbers(1000001)
