#!/usr/bin/env python3
with open("day3-input.txt") as input_file:
    input = input_file.readlines()
    cleaned = [line.rstrip() for line in input]
# print(cleaned)

v1t = 0
v1f = 0

values = {}
measures = {}
most_common = {}
least_common = {}
gamma_binary = ""
epsilon_binary = ""
# test = cleaned[0]
# print(test)
# for i in range(len(test)):
#     print(test[i])

for i in range(len(cleaned[0])):
    values[i] = []
    measures[i] = 0
    most_common[i] = 0

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

# for key, value in measures:
#     print(key, value)
# print(values)

for i in measures:
    if measures[i] > 500:
        most_common[i] = 1
        least_common[i] = 0
    else:
        most_common[i] = 0
        least_common[i] = 1

for i in most_common:
    gamma_binary = gamma_binary + str(most_common[i])
for i in least_common:
    epsilon_binary = epsilon_binary + str(least_common[i])

print(gamma_binary)
gamma_rate = int(gamma_binary, 2)
print(gamma_rate)

print(epsilon_binary)
epsilon_rate = int(epsilon_binary, 2)
print(epsilon_rate)

answer_1 = gamma_rate * epsilon_rate
print(f'The part 1 answer is {answer_1}')