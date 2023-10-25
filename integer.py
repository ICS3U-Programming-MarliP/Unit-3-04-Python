#!usr/bin/env python3
# Created By: Marli Peters
# Date: Oct. 25, 2023
# This program asks the user for a number then
# tells them if the number is positive or negative.


def main():
    # get user guess
    number = int(input("Enter integer: "))
    print("")

    # check if guess is correct
    if number < 0:
        print("{} is a negative number!".format(number))

    elif number > 0:
        print("{} is a positive number!".format(number))

    else:
        print("0 is just 0!")


if __name__ == "__main__":
    main()
