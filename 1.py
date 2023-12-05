file_path = './1_data.txt'

# Pt 1
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
line_sum = 0
with open(file_path, 'r') as file:
    file_contents = file.read()
    for line in file_contents.splitlines():
        digits_in_line = [c for c in line if c in digits]
        if len(digits_in_line) == 0:
            continue
        elif len(digits_in_line) == 1:
            digits_as_str = digits_in_line[0] + digits_in_line[0]
        else:
            digits_as_str = digits_in_line[0] + digits_in_line[-1]
        line_sum += int(digits_as_str)
    print("Part 1: " + str(line_sum))

digit_map = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
digits_sum = 0
with open(file_path, 'r') as file:
    file_contents = file.read()
    for line in file_contents.splitlines():
        lowest_index_and_digit = len(line), ""
        highest_index_and_digit = -1, ""

        for digit in digit_map:
            left_index = line.find(digit)
            right_index = line.rfind(digit)
            if left_index != -1 and left_index < lowest_index_and_digit[0]:
                lowest_index_and_digit = left_index, digit_map[digit]
            if right_index != -1 and right_index > highest_index_and_digit[0]:
                highest_index_and_digit = right_index, digit_map[digit]

        if lowest_index_and_digit[1] != "" and highest_index_and_digit[1] != "":
            digits_sum += int(lowest_index_and_digit[1] + highest_index_and_digit[1])

    print("Part 2: " + str(digits_sum))
                
        
