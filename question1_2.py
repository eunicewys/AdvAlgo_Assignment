import random


def hash_ic_number(ic_number):
    part1 = int(ic_number[0:3])
    part2 = int(ic_number[3:6])
    part3 = int(ic_number[6:9])
    part4 = int(ic_number[9:12])
    return part1 + part2 + part3 + part4

def generate_random_ic():
    return ''.join(random.choices('0123456789', k=12))

def insert_into_hash_table(table_size, ic_list):
    hash_table = [[] for _ in range(table_size)]
    collision_count = 0

    for ic in ic_list:
        hash_code = hash_ic_number(ic)
        index = hash_code % table_size

        if len(hash_table[index]) > 0:
            collision_count += 1

        hash_table[index].append(ic)

    return collision_count, hash_table


def main():
    print("=== Hash Table Collision Test (10 rounds) ===")
    table_sizes = [1009, 2003]

    for round_num in range(1, 11): 
        print(f"\n--- Round {round_num} ---")
        ic_numbers = [generate_random_ic() for _ in range(1000)]

        for size in table_sizes:
            collisions, table = insert_into_hash_table(size, ic_numbers)
            print(f"Table size {size}: {collisions} collisions")


if __name__ == "__main__":
    main()
