import random
import threading
import time


def generate_random_numbers():
    numbers = []
    for _ in range(100):
        numbers.append(random.randint(0, 10000))
    numbers.sort()
    return numbers


def thread_task(result_list, index):
    result_list[index] = generate_random_numbers()

def run_combined_test():
    multithread_times = []
    non_multithread_times = []
    differences = []

    print("\nRound-by-Round Performance Comparison:")
    print("+--------+----------------------------+-----------------------------+------------------------+")
    print("| Round  | Multithreading Time (ns)   | Non-Multithreading Time (ns) | Difference (ns)       |")
    print("+--------+----------------------------+-----------------------------+------------------------+")

    for round_num in range(1, 11):

        thread_results = [None] * 3
        threads = []

        mt_start = time.time_ns()
        for i in range(3):
            t = threading.Thread(target=thread_task, args=(thread_results, i))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        mt_end = time.time_ns()
        mt_time = mt_end - mt_start
        multithread_times.append(mt_time)


        nt_start = time.time_ns()
        set1 = generate_random_numbers()
        set2 = generate_random_numbers()
        set3 = generate_random_numbers()
        nt_end = time.time_ns()
        nt_time = nt_end - nt_start
        non_multithread_times.append(nt_time)


        diff = nt_time - mt_time
        differences.append(diff)

        print(f"| {round_num:<6} | {mt_time:<26} | {nt_time:<27}  | {diff:<22}|")

    print("+--------+----------------------------+-----------------------------+------------------------+")


    mt_total = sum(multithread_times)
    nt_total = sum(non_multithread_times)
    diff_total = sum(differences)

    mt_avg = mt_total / 10
    nt_avg = nt_total / 10
    diff_avg = diff_total / 10

    print("\nSummary of Results:")
    print("+----------------+----------------------------+-----------------------------+------------------------+")
    print("| Metric         | Multithreading (ns)        | Non-Multithreading (ns)     | Difference (ns)        |")
    print("+----------------+----------------------------+-----------------------------+------------------------+")
    print(f"| Total Time     | {mt_total:<26} | {nt_total:<27} | {diff_total:<22} |")
    print(f"| Average Time   | {mt_avg:<26.1f} | {nt_avg:<27.1f} | {diff_avg:<22.1f} |")
    print("+----------------+----------------------------+-----------------------------+------------------------+")


if __name__ == "__main__":
    run_combined_test()
