import random
import threading
import time

def generate_random_num():
    numbers = []
    for _ in range(100):
        num = random.randint(0, 10000)
        numbers.append(num)
    numbers.sort()
    return numbers

def thread_task(result_list, index):
    result_list[index] = generate_random_num()

def multithreading_test():
    round_times = []

    print("\n+--------------------------------------------------------------+")
    print("| Round  |      Multithreading Time (ns)                       |")
    print("+--------------------------------------------------------------+")

    for round_num in range(1, 11):
        results = [None] * 3
        threads = []

        t1 = time.time_ns()


        for i in range(3):
            thread = threading.Thread(target=thread_task, args=(results, i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        t2 = time.time_ns()
        time_taken = t2 - t1
        round_times.append(time_taken)

        print(f"|   {round_num:<4} |        {time_taken:<43}  |")

    print("+--------------------------------------------------------------+")


    total_time = sum(round_times)
    average_time = total_time / len(round_times)

    print("\nSummary of Results:")
    print("+----------------+--------------------------+")
    print("| Metric         | Multithreading (ns)      |")
    print("+----------------+--------------------------+")
    print(f"| Total Time     | {total_time:<24} |")
    print(f"| Average Time   | {average_time:<24.1f} |")
    print("+----------------+--------------------------+")


if __name__ == "__main__":
    multithreading_test()
