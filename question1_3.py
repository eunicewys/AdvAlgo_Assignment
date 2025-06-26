import random

# Hash function using folding technique
def hash_ic_number(ic_number):
    part1 = int(ic_number[0:3])
    part2 = int(ic_number[3:6])
    part3 = int(ic_number[6:9])
    part4 = int(ic_number[9:12])
    return part1 + part2 + part3 + part4

def generate_random_ic():
    return ''.join(random.choices('0123456789', k=12))

def print_hash_table_sample(table, table_size, sample_limit=10):

    random_indexes = random.sample(range(table_size), 30)
    filled_samples = []

    for i in random_indexes:
        if table[i]:
            filled_samples.append(i)
        if len(filled_samples) >= sample_limit:
            break

    filled_samples.sort()

    print(f"\nSample Entries for Table {table_size}: ")
    if filled_samples:
        for i in filled_samples:
            print(f"table[{i:<4}] --> {' --> '.join(table[i])}")
    else:
        print("No entries found in sampled indexes. Showing fallback entries:")
        count = 0
        for i in range(table_size):
            if table[i]:
                print(f"table[{i:<4}] --> {' --> '.join(table[i])}")
                count += 1
                if count >= sample_limit:
                    break



def main():
    print("\n============================================================")
    print("          10 Rounds of Hash Table Collision Test")
    print("============================================================")

    table_sizes = [1009, 2003]
    total_collisions = {1009: 0, 2003: 0}
    total_filled_slots = {1009: 0, 2003: 0}
    round_collisions = []

    for round_num in range(1, 11):
        print(f"\n============================================================")
        print(f"                Round {round_num} ")
        print(f"============================================================")

        ic_numbers = [generate_random_ic() for _ in range(1000)]


        table_1009 = [[] for _ in range(1009)]
        table_2003 = [[] for _ in range(2003)]
        collisions_1009 = 0
        collisions_2003 = 0

        for ic in ic_numbers:
            h1 = hash_ic_number(ic) % 1009
            if table_1009[h1]:
                collisions_1009 += 1
            table_1009[h1].append(ic)

            h2 = hash_ic_number(ic) % 2003
            if table_2003[h2]:
                collisions_2003 += 1
            table_2003[h2].append(ic)


        filled_1009 = sum(1 for bucket in table_1009 if bucket)
        filled_2003 = sum(1 for bucket in table_2003 if bucket)
        total_filled_slots[1009] += filled_1009
        total_filled_slots[2003] += filled_2003

        total_collisions[1009] += collisions_1009
        total_collisions[2003] += collisions_2003
        total_round = collisions_1009 + collisions_2003
        round_collisions.append(total_round)

        print(f"\n[Table Size: 1009]")
        print(f"Total Collisions  : {collisions_1009}")
        print(f"Filled Slots      : {filled_1009} / 1009")
        print(f"Collision Rate    : {(collisions_1009 / 1000) * 100:.2f} %")

        print(f"\n[Table Size: 2003]")
        print(f"Total Collisions  : {collisions_2003}")
        print(f"Filled Slots      : {filled_2003} / 2003")
        print(f"Collision Rate    : {(collisions_2003 / 1000) * 100:.2f} %")

        print("\n------------------------------------------------------------")
        print_hash_table_sample(table_1009, 1009)
        print_hash_table_sample(table_2003, 2003)
        print("------------------------------------------------------------")


    print("\n\n\n============================================================")
    print("               Final Summary After 10 Rounds")
    print("============================================================")

    for size in table_sizes:
        avg_collisions = total_collisions[size] / 10
        avg_filled = total_filled_slots[size] / 10
        collision_rate = (avg_collisions / 1000) * 100
        print(f"[Table Size {size}]")
        print(f"Average Collisions      : {avg_collisions:.2f}")
        print(f"Average Filled Slots    : {avg_filled:.2f} / {size}")
        print(f"Average Collision Rate  : {collision_rate:.2f} %\n")

    print("Total combined collisions for each round:")
    for i, total in enumerate(round_collisions, 1):
        print(f"Round {i:<2}: {total} total collisions")
    print("============================================================")

if __name__ == "__main__":
    main()



