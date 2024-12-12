#!/usr/bin/env python3

input_file="input/puzzle2.txt"
#input_file = "safety_test.txt"

def check_if_safe(report, incr_or_decr="empty"):
    "A report is safe if all numbers are either increasing or decreasing by at least one and at most 3."

    number = int(report[0])
    #print(report)
    #print(incr_or_decr)
    #print(number)

    #for next_nr in report[1:]:
    next_nr = int(report[1])
    if next_nr == number:
        return "Unsafe"

    elif next_nr > number:
        if incr_or_decr == "decrease":
            return "Unsafe"
        else:
            incr_or_decr = "increase"

        if next_nr - number > 3:
            return "Unsafe"
        else:
            pass

        if len(report[1:]) > 1:
            return check_if_safe(report[1:], "increase")
        elif len(report[1:]) == 1:
            return "Safe"
        else:
            print("What is left of my report?")
            print(report)


    elif next_nr < number:
        if incr_or_decr == "increase":
            return "Unsafe"
        else:
            incr_or_decr = "decrease"

        if number - next_nr > 3:
            return "Unsafe"
        else:
            pass

        if len(report[1:]) > 1:
            return check_if_safe(report[1:], "decrease")
        else:
            return "Safe"

    else:
        return "Found no answer?"

safety_list = []
safety_dict = {}

with open(input_file, "r") as infile:
    for report in infile:
        report = report.split()

        safety = check_if_safe(report)

        safety_list.append(safety)

        if safety in safety_dict.keys():
            safety_dict[safety] += 1
        else:
            safety_dict[safety] = 1

print(safety_list)

print(safety_dict)
