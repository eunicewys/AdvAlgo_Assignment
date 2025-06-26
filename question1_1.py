def hash_ic_number(ic_number):
    if len(ic_number) != 12 or not ic_number.isdigit():
        print("Invalid IC number! Please enter a 12-digit number without dash")
        return None

    part1 = int(ic_number[0:3])
    part2 = int(ic_number[3:6])
    part3 = int(ic_number[6:9])
    part4 = int(ic_number[9:12])

    hash_code = part1 + part2 + part3 + part4

    return hash_code


def main():
    print("=== Malaysian IC Hashing Program ===")
    ic_input = input("Enter a 12-digit Malaysian IC number (no dashes): ")

    result = hash_ic_number(ic_input)

    if result is not None:
        print("Hash Code for IC number:", result)


if __name__ == "__main__":
    main()