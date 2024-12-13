target = input("What is your Target for max Prime?: ")
number_list = []
number = 0
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

while target > 0:
    prime = is_prime(number)
    if prime is True:
        number_list.append(number)
    number += 1
    target -= 1
    
max_prime = max(number_list)
print(max_prime)
