# Define the file path
file_path = './2_data.txt'

# Pt 1
valid_games_sum = 0
with open(file_path, 'r') as file:
    file_contents = file.read()
    for line in file_contents.splitlines():
        game_number, turns_raw = line.split(":")
        game_number = int(game_number.strip("Game "))
        turns = turns_raw.split(";")
        valid = True
        for turn in turns:
            num_and_colors = turn.split(",")
            for num_and_color in num_and_colors:
                num, color = num_and_color.strip().split(" ")
                num = int(num)
                if color == "blue" and num > 14:
                    valid = False
                elif color == "green" and num > 13:
                    valid = False
                elif color == "red" and num > 12:
                    valid = False
        if valid:
            valid_games_sum += game_number
    print("Part 1: " + str(valid_games_sum))


# Pt 2
powers_sum = 0
with open(file_path, 'r') as file:
    file_contents = file.read()
    for line in file_contents.splitlines():
        game_number, turns_raw = line.split(":")
        game_number = int(game_number.strip("Game "))
        turns = turns_raw.split(";")
        red_counts = []
        green_counts = []
        blue_counts = []
        for turn in turns:
            num_and_colors = turn.split(",")
            for num_and_color in num_and_colors:
                num, color = num_and_color.strip().split(" ")
                num = int(num)
                if color == "blue":
                    blue_counts.append(num)
                elif color == "green":
                    green_counts.append(num)
                elif color == "red":
                    red_counts.append(num)
        powers_sum += max(red_counts) * max(green_counts) * max(blue_counts)
    print("Part 2: " + str(powers_sum))
                    
            
