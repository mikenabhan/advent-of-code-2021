#!/usr/bin/env python3
with open("day3-input.txt") as input_file:
    input = input_file.readlines()
    cleaned = [line.rstrip() for line in input]
# print(cleaned)

v1t = 0
v1f = 0

values = {}
measures = {}

# test = cleaned[0]
# print(test)
# for i in range(len(test)):
#     print(test[i])

for i in range(len(cleaned[0])):
    values[i] = []
    measures[i] = 0

for line in cleaned:
    for character in range(len(line)):
        # print(line[character])
#         values[character[line[character]]]
        values[character].append(line[character])

for i in values:
    for j in values[i]:
        if j == '1':
            measures[i] += 1
print(measures)
    # print(len(values[i]))

for key, value in measures:
    print(key, value)
# print(values)

