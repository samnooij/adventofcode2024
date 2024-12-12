#!/usr/bin/env python3

import re

input_file = "input/puzzle3.txt"

def mul(x, y):
    return x * y

overall_pattern = r"mul\([0-9]*,[0-9]*\)"

numbers_pattern = r"mul\(([0-9]*),([0-9]*)\)"

total_sum = 0

with open(input_file, "r") as infile:
    for line in infile:
        hit_list = re.findall(overall_pattern, line)
        for hits in hit_list:
            first_number = int(re.search(numbers_pattern, hits).group(1))
            second_number = int(re.search(numbers_pattern, hits).group(2))

            total_sum += mul(first_number, second_number)

print("Total sum is (for the first part):")
print(total_sum)


## Part 2:

do_dont_pattern = r"mul\([0-9]*,[0-9]*\)|don't\(\)|do\(\)"

setting = "do"

match_list = []

with open(input_file, "r") as infile:
    for line in infile:
        hit_list = re.findall(do_dont_pattern, line)

        for hit in hit_list:
            match_list.append(hit)

conditional_sum = 0

for element in match_list:
    if setting == "do":
        if element == "do()":
            pass
        elif element == "don't()":
            setting = "dont"
        else:
            first_number = int(re.search(numbers_pattern, element).group(1))
            second_number = int(re.search(numbers_pattern, element).group(2))
            conditional_sum += mul(first_number, second_number)
    elif setting == "dont":
        if element == "do()":
            setting = "do"
        else:
            pass

print("Sum taking into account dos and don'ts:")
print(conditional_sum)
