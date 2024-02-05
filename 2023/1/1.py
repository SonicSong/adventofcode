import re

input_file = open("input", "r")
lines = input_file.readlines()
line_count = 0
list_elements = []

def regex(line):
    fin_lines_maybe = re.findall(r'\d', line)
    res1 = [fin_lines_maybe[0]]
    res2 = [fin_lines_maybe[-1]]
    join_res = (res1 + res2)
    fin_res = int("".join(join_res))
    list_elements.append(fin_res)


def counting(line_elements):
    Sum = sum(line_elements)
    print(Sum)


for line in lines:
    line_count += 1
    regex(line)

counting(list_elements)
