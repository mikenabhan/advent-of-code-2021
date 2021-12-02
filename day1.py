#!/usr/bin/env python3
increases = 0
with open("day1-input.txt") as input_file:
    input = input_file.readlines()
    cleaned = [line.rstrip() for line in input]
# print(cleaned)
cleaned_ints = [int(i) for i in cleaned]
previous_value = cleaned_ints[0]


# for index, value in enumerate(cleaned_ints):
#     if cleaned_ints[index] > previous_value:
#         increases += 1
#     previous_value = cleaned_ints[index]



for index, value in enumerate(cleaned_ints):
    if cleaned_ints[index - 1] < cleaned_ints[index]:
        increases += 1

print(f'The answer to part one is: {increases}')

sums = 0

# ##PART TWO
rolling_indices = [0, 1, 2]
previous_range = [cleaned_ints[i] for i in rolling_indices]
# print(previous_range)
for index, value in enumerate(cleaned_ints):
    new_indices = []
    for i in rolling_indices:
        if i + 1 > len(cleaned_ints):
            i = 0
        else:
            new_indices.append(i + 1)
    # print(new_indices)
    working_range = [cleaned_ints[i - 1] for i in new_indices]
    print(sum(working_range),sum(previous_range))
    if sum(working_range) > sum(previous_range):
        sums += 1
    rolling_indices = new_indices
    previous_range = [cleaned_ints[i - 1] for i in rolling_indices]



# for index, value in enumerate(cleaned_ints):
#     newindex = index + 1
#     workinglist = []
#     nextlist = []
#     workinglist.append(cleaned_ints[index])
#     workinglist.append(cleaned_ints[index + 1])
#     workinglist.append(cleaned_ints[index + 2])
#     nextlist.append(cleaned_ints[newindex])
#     nextlist.append(cleaned_ints[newindex + 1])
#     nextlist.append(cleaned_ints[newindex + 2])

    # working_value= sum(cleaned_ints[index],cleaned_ints[index + 1],cleaned_ints[index + 2])
    # next_value = sum(cleaned_ints[newindex],cleaned_ints[newindex + 1],cleaned_ints[newindex + 2])

#     if sum(workinglist) < sum(nextlist):
#         sums += 1

print(f'The answer to part two is: {sums}')