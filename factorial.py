#!/usr/bin/env python3
# Created By: Lennon Cehajic
# Date: November 13th, 2026
# This program calculates the factorial of a whole number.
#
def main():
    # Initialization
    loop_counter = 0
    factorial_answer = 1

    # Get the user input as a string.
    user_number_string = input(
        "Welcome to Lennon’s factorial calculator. Please enter a whole number: "
    )

    # Try converting the input to an integer, calculate the factorial,
    # then display the result.
    try:
        user_number_int = int(user_number_string)
        if user_number_int < 0:
            print(
                "{} is not a positive number. Please enter a valid number.".format(
                    user_number_int
                )
            )
        else:
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} times through loop.".format(loop_counter))
                if loop_counter >= user_number_int:
                    break

            print("{}! = {}".format(user_number_int, factorial_answer))

    except Exception:
        print("{} is not a valid whole number".format(user_number_string))

    finally:
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
