import random

def generate_random_numbers():
    numbers = [] 
    for _ in range(100):
        num = random.randint(0, 10000)
        numbers.append(num)
    return numbers

random_list = generate_random_numbers()

print("Generated 100 random numbers:")
print(random_list)
