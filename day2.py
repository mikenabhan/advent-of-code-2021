#!/usr/bin/env python3
increases = 0
with open("day2-input.txt") as input_file:
    input = input_file.readlines()
    cleaned = [line.rstrip() for line in input]
# print(cleaned)

coordinates = {'position': 0, 'depth': 0}

def parse_direction(direction):
    parsed = direction.split(' ')
    formatted = [parsed[0], int(parsed[1])]
    return formatted

def run_direction(formatted_direction):
    if formatted_direction[0] == 'up':
        if coordinates['depth'] - formatted_direction[1] < 0:
            coordinates['depth'] = 0
        else:
            coordinates['depth'] = coordinates['depth'] - formatted_direction[1]
    elif formatted_direction[0] == 'down':
        coordinates['depth'] = coordinates['depth'] + formatted_direction[1]
    elif formatted_direction[0] == 'forward':
        coordinates['position'] = coordinates['position'] + formatted_direction[1]
    else:
        print("Something did not work")

for i in cleaned:
    run_direction(parse_direction(i))

print(coordinates)
answer = coordinates['position'] * coordinates ['depth']
print(f'The part 1 answer is {answer}')


# print(parse_direction(cleaned[0]))

# obj = parse_direction(cleaned[0])
# print(type(obj[1]))

####PART TWO####

coordinates_2 = {'position': 0, 'depth': 0, 'aim': 0}

def run_direction_2(formatted_direction):
    if formatted_direction[0] == 'up':
        coordinates_2['aim'] = coordinates_2['aim'] - formatted_direction[1]
    elif formatted_direction[0] == 'down':
        coordinates_2['aim'] = coordinates_2['aim'] + formatted_direction[1]
    elif formatted_direction[0] == 'forward':
        coordinates_2['position'] = coordinates_2['position'] + formatted_direction[1]
        coordinates_2['depth'] = coordinates_2['aim'] * formatted_direction[1] + coordinates_2['depth']
        if coordinates_2['depth'] < 0:
            coordinates_2['depth'] = 0
    else:
        print("Something did not work")

for i in cleaned:
    run_direction_2(parse_direction(i))

print(coordinates_2)
answer2 = coordinates_2['position'] * coordinates_2['depth']
print(f'The part 2 answer is {answer2}')