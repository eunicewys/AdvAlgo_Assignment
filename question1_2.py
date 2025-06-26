import random

# Hash function using folding technique
def hash_ic_number(ic_number):
    part1 = int(ic_number[0:3])
    part2 = int(ic_number[3:6])
    part3 = int(ic_number[6:9])
    part4 = int(ic_number[9:12])
    return part1 + part2 + part3 + part4

# Generate a random 12-digit IC number
def generate_random_ic():
    return ''.join(random.choices('0123456789', k=12))

# Insert IC numbers into the hash table and count collisions
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

# Print a few random sample entries from the hash table (sorted)
def print_hash_table_sample(table, table_size, sample_limit=10):
    random_indexes = random.sample(range(table_size), 30)
    filled_samples = []

    for i in random_indexes:
        if table[i]:
            filled_samples.append(i)
        if len(filled_samples) >= sample_limit:
            break

    filled_samples.sort()

    print(f"\nSample Entries for Table {table_size}:")
    if filled_samples:
        for i in filled_samples:
            print(f"table[{i:<4}] --> {' --> '.join(table[i])}")
    else:
        print("No filled entries found.")

# Main program
def main():
    print("\n=== 10 Rounds of Collision Test ===")
    table_sizes = [1009, 2003]
    total_collisions = {1009: 0, 2003: 0}

    for round_num in range(1, 11):
        print(f"\n--- Round {round_num} ---")
        ic_numbers = [generate_random_ic() for _ in range(1000)]

        for size in table_sizes:
            collisions, table = insert_into_hash_table(size, ic_numbers)
            total_collisions[size] += collisions
            print(f"\nTable size {size}: {collisions} collisions")
            print_hash_table_sample(table, size)

    print("\n=== Average collisions for each table ===")
    for size in table_sizes:
        avg = total_collisions[size] / 10
        print(f"Average for table size {size}: {avg:.2f}")

if __name__ == "__main__":
    main()

