import random

def generate_sorted_random_numbers():
    numbers = []
    for _ in range(100):
        num = random.randint(0, 10000)
        numbers.append(num)
    numbers.sort()
    return numbers

sorted_random_list = generate_sorted_random_numbers()

print("100 Sorted Random Numbers (0 to 10,000):")
print(sorted_random_list)
