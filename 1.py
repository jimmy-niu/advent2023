file_path = './1_small_data.txt'

# Pt 1
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# line_sum = 0
# with open(file_path, 'r') as file:
#     file_contents = file.read()
#     for line in file_contents.splitlines():
#         digits_in_line = [c for c in line if c in digits]
#         if len(digits_in_line) == 0:
#             continue
#         elif len(digits_in_line) == 1:
#             digits_as_str = digits_in_line[0] + digits_in_line[0]
#         else:
#             digits_as_str = digits_in_line[0] + digits_in_line[-1]
#         line_sum += int(digits_as_str)
#     print("Part 1: " + str(line_sum))

digit_map = {
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
        digit_to_index = {}
        for digit in digit_map:
            digit_index = line.find(digit)
            if digit_index != -1:
                digit_to_index[digit] = digit_index
        sorted_digit_to_index = dict(sorted(digit_to_index.items(), key=lambda item: item[1]))
        for _ in range(2):
            for digit in sorted_digit_to_index:
                line = line.replace(digit, digit_map[digit])
        
        digits_in_line = [c for c in line if c in digits]
        if len(digits_in_line) == 0:
            continue
        elif len(digits_in_line) == 1:
            digits_as_str = digits_in_line[0] + digits_in_line[0]
        else:
            digits_as_str = digits_in_line[0] + digits_in_line[-1]
        digits_sum += int(digits_as_str)
    print("Part 2: " + str(digits_sum))
                
        
