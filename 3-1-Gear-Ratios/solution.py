def sum_part_numbers_corrected(schematic):
    lines = schematic.strip().split('\n')
    symbols = set("1234567890.")

    # Function to check if a given position has an adjacent symbol
    def has_adjacent_symbol(x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if 0 <= x + dx < len(lines) and 0 <= y + dy < len(lines[x + dx]):
                    if lines[x + dx][y + dy] not in symbols:
                        return True
        return False

    # Keep track of which numbers have been counted
    counted = set()

    # Summing up all the part numbers
    total = 0
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y].isdigit() and (x, y) not in counted:
                # Find the entire number
                start = y
                while start > 0 and lines[x][start - 1].isdigit():
                    start -= 1

                end = y
                while end < len(lines[x]) - 1 and lines[x][end + 1].isdigit():
                    end += 1

                number = int(lines[x][start:end + 1])

                # Check if the number is adjacent to a symbol
                if any(has_adjacent_symbol(x, i) for i in range(start, end + 1)):
                    total += number
                    # Marking all digits of this number as counted
                    for i in range(start, end + 1):
                        counted.add((x, i))
    print(counted)
    return total


engine_schematic = open('input.txt').read()
print(sum_part_numbers_corrected(engine_schematic))
