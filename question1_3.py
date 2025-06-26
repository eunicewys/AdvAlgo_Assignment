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
    collision_count =0

    for ic in ic_list:
        hash_code = hash_ic_number(ic)
        index = hash_code % table_size

        if len(hash_table[index]) > 0:
            collision_count += 1

        hash_table[index].append(ic)

    return collision_count


def main():
    print("\n=== 10 round of collision test ===\n")

    table_sizes = [1009, 2003]
    total_collisions = {1009: 0, 2003: 0}
    round_collisions = []

    for round_num in range(1, 11):
        print(f"- Round {round_num} -")
        ic_numbers = [generate_random_ic() for _ in range(1000)]

        collisions_1009 = insert_into_hash_table(1009, ic_numbers)
        collisions_2003 = insert_into_hash_table(2003, ic_numbers)

        total_collisions[1009] += collisions_1009
        total_collisions[2003] += collisions_2003

        total_round = collisions_1009 + collisions_2003
        round_collisions.append(total_round)

        print(f"Table size 1009: {collisions_1009} collisions")
        print(f"Table size 2003: {collisions_2003} collisions")
        print(f"Total collisions for round {round_num}: {total_round}\n")


    avg_1009 = total_collisions[1009] /10
    avg_2003 = total_collisions[2003] /10

    print("=== Summary After 10 Rounds ===")
    print(f"Average collisions for table size 1009: {avg_1009:.2f}")
    print(f"Average collisions for table size 2003: {avg_2003:.2f}\n")

    print("\n=== Total collisions Per Round ===")
    for i, total in enumerate(round_collisions, 1):
        print(f"Round {i}: {total} total collisions")


if __name__ == "__main__":
    main()


