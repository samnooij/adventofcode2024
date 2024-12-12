#!/usr/bin/env python3

import re

input_file = "input/puzzle3.txt"

def mul(x, y):
    return x * y

overall_pattern = r"mul\([0-9]*,[0-9]*\)"

numbers_pattern = r"mul\(([0-9]*),([0-9]*)\)"

matches = []

total_sum = 0

with open(input_file, "r") as infile:
    for line in infile:
        hit_list = re.findall(overall_pattern, line)
        for hits in hit_list:
            first_number = int(re.search(numbers_pattern, hits).group(1))
            second_number = int(re.search(numbers_pattern, hits).group(2))

            total_sum += mul(first_number, second_number)

print(total_sum)
