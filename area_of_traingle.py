#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program calculates the area of a triangle
#    with user input

import math


def main():
    # main function
    print("We will be calculating the area of a triangle.")

    # input
    base = int(input("Enter the base (mm):"))
    height = int(input("Enter the height (mm):"))

    # process
    area = base * height / 2

    # output
    print("Area is {} mm^2".format(area))


if __name__ == "__main__":
    main()
