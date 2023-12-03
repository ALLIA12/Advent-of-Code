import re


def readFile(file_path):
    string_array = []
    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading and trailing whitespace (e.g., newline characters)
            line = line.strip()

            string_array.append(line)

    return string_array


def processStr(str):
    parts = str.split(':', 1)
    game_part = parts[0]
    game_id_parts = game_part.split()
    game_id = game_id_parts[-1] if len(game_id_parts) > 1 else None
    color_counts_part = parts[1] if len(parts) > 1 else ""
    color_counts_segments = color_counts_part.split(';')
    color_counts_segments = [segment.strip() for segment in color_counts_segments]
    return game_id, color_counts_segments


def getOneRowVal(str):
    game_id, color_counts_segments = processStr(str)
    # Regular expression pattern to match a number followed by a color
    pattern = r'(\d+)\s+(red|blue|green)'
    minRed = minGreen = minBlue = -1
    # Loop through each string and extract numbers and corresponding colors
    for color_string in color_counts_segments:
        matches = re.findall(pattern, color_string)
        for match in matches:
            if match[1] == 'red':
                if int(match[0]) > minRed:
                    minRed = int(match[0])
            elif match[1] == 'green':
                if int(match[0]) > minGreen:
                    minGreen = int(match[0])
            elif match[1] == 'blue':
                if int(match[0]) > minBlue:
                    minBlue = int(match[0])
    return minBlue * minGreen * minRed


def getSum(string_array):
    sum = 0
    for str in string_array:
        sum += getOneRowVal(str)
    return sum


if __name__ == "__main__":
    string_array = readFile('input.txt')
    result = getSum(string_array)
    print(result)
