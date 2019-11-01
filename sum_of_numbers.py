#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program guesses random numbers


def main():
    # this function guesses random numbers
    sum_of_numbers = 0

    # input
    integer_as_string = input("How many numbers are going to add (integer): ")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        for loop_counter in range(integer_as_number):
            entered_number = int(input("Enter a number to add: "))
            if entered_number < 0:
                continue
            else:
                sum_of_numbers = sum_of_numbers + entered_number
        print("Sum of just the positive numbers is = {}".format(sum_of_numbers))
    except Exception:
        print("It is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
