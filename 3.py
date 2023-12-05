file_path = './3_data.txt'

# Omitting the period as that is not considered a symbol in our schematics. 
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", "?", "/", "~", "`"]
processed_grid = []
# Pt 1
with open(file_path, 'r') as file:
    file_contents = file.read()
    for row_index, line in enumerate(file_contents.splitlines()):
        for col_index, c in enumerate(line):
            if row_index == len(processed_grid):
                processed_grid.append([])
            processed_grid[row_index].append(c)

part_number_sum = 0

# Something I learned while debugging part 1 (as maybe hinted at by small_data_2):
#  int'ing 05 -> 5 which is bad, since we drop a number in case it's 105. In the original code, 
#  that would have turned into 15, which is wrong.
def check_and_set_to_period(row_index, col_index):
    if row_index < 0 or row_index >= len(processed_grid):
        return "-1"
    if col_index < 0 or col_index >= len(processed_grid[row_index]):
        return "-1"
    try:
        value = int(processed_grid[row_index][col_index])
        processed_grid[row_index][col_index] = "."
        left_value = check_and_set_to_period(row_index, col_index - 1)
        right_value = check_and_set_to_period(row_index, col_index + 1)
        final_value = str(value)
        
        if left_value != "-1":
            final_value = str(left_value) + final_value
        if right_value != "-1":
            final_value += str(right_value)
        return final_value
    except ValueError:
        return "-1"

for row_index in range(len(processed_grid)):
    for col_index in range(len(processed_grid[row_index])):
        if processed_grid[row_index][col_index] in symbols:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    value = check_and_set_to_period(row_index + i, col_index + j)
                    if value != "-1":
                        part_number_sum += int(value)
                        print(value)

print("Part 1: " + str(part_number_sum))