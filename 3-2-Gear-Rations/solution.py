def sum_gear_ratios(schematic):
    lines = schematic.strip().split('\n')

    # Function to find all part numbers adjacent to a given position
    def adjacent_part_numbers(x, y):
        part_numbers = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(lines) and 0 <= ny < len(lines[nx]) and lines[nx][ny].isdigit():
                    # Find the entire number
                    start = ny
                    while start > 0 and lines[nx][start - 1].isdigit():
                        start -= 1

                    end = ny
                    while end < len(lines[nx]) - 1 and lines[nx][end + 1].isdigit():
                        end += 1

                    number = int(lines[nx][start:end + 1])

                    # Adding unique part numbers only
                    if number not in part_numbers:
                        part_numbers.append(number)

        return part_numbers

    # Summing up all the gear ratios
    total = 0
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] == '*':
                part_numbers = adjacent_part_numbers(x, y)
                # A gear is valid if it's adjacent to exactly two part numbers
                if len(part_numbers) == 2:
                    gear_ratio = part_numbers[0] * part_numbers[1]
                    total += gear_ratio

    return total


engine_schematic = open('input.txt').read()
print(sum_gear_ratios(engine_schematic))
