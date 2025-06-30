import random
import time


def generate_sorted_random_numbers():
    numbers = []
    for _ in range(100):
        num = random.randint(0, 10000)
        numbers.append(num)
    numbers.sort()
    return numbers


def non_multithreading_test():
    round_times = []

    print("\n+--------------------------------------------------------------+")
    print("| Round | Non-Multithreading Time (ns)                         |")
    print("+--------------------------------------------------------------+")

    for round_num in range(1, 11):
        t1 = time.time_ns()

        set1 = generate_sorted_random_numbers()
        set2 = generate_sorted_random_numbers()
        set3 = generate_sorted_random_numbers()

        t2 = time.time_ns()
        time_taken = t2 - t1
        round_times.append(time_taken)

        print(f"|   {round_num:<4} | {time_taken:<43} |")

    print("+--------------------------------------------------------------+")

    total_time = sum(round_times)
    average_time = total_time / len(round_times)

    print("\nSummary of Results:")
    print("+----------------+-----------------------------+")
    print("| Metric         | Non-Multithreading (ns)     |")
    print("+----------------+-----------------------------+")
    print(f"| Total Time     | {total_time:<27} |")
    print(f"| Average Time   | {average_time:<27.1f} |")
    print("+----------------+-----------------------------+")


if __name__ == "__main__":
    non_multithreading_test()
