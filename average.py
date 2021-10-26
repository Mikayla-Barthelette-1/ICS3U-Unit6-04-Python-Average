#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program finds the average of all of the numbers inside a 2D array

import random


def average_of_numbers(passed_in_2D_list):
    # this function finds the average of the numbers in the 2D array

    row = len(passed_in_2D_list)
    column = len(passed_in_2D_list[0])
    amount_of_numbers = row * column
    the_sum = 0
    for row_value in passed_in_2D_list:
        for single_number in row_value:
            the_sum = the_sum + single_number

    the_average = the_sum / amount_of_numbers

    return the_average


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    print("Starting ...")
    print("")
    user_input0 = input("How many rows would you like: ")
    user_input1 = input("How many columns would you like: ")
    print("")

    try:
        rows = int(user_input0)
        columns = int(user_input1)
        for loop_counter_rows in range(0, rows):
            temp_column = []
            for loop_counter_columns in range(0, columns):
                a_random_number = random.randint(0, 10)
                temp_column.append(a_random_number)
                print("{0} ".format(a_random_number), end="")
            a_2d_list.append(temp_column)
            print("")
    except (Exception):
        print("Invalid input.")
        print("\nDone.")
        exit()
    finally:
        None

    average = average_of_numbers(a_2d_list)
    print("\nThe average of all the numbers is: {0} ".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
