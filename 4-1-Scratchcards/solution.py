def split_card_data(card_string):
    # Splitting the string into card number and data
    card_number, card_data = card_string.split(': ')

    # Further splitting the data based on the '|' character
    before_after_split = card_data.split('|')

    # Converting each part into individual elements and then into integers
    before_array = [int(x) for x in before_after_split[0].split()]
    after_array = [int(x) for x in before_after_split[1].split()]

    return card_number, before_array, after_array


def processLine(line):
    _, winning, numbers = split_card_data(line)
    matches = -1
    for number in numbers:
        if number in winning:
            matches += 1
    if matches == -1:
        return 0
    else:
        return 2 ** matches


def getSum(lines):
    sum = 0
    for line in lines:
        curr = processLine(line)
        #print(curr)
        sum += curr
    return sum


if __name__ == '__main__':
    input_cards = open('input.txt').read()
    lines = input_cards.strip().split('\n')
    result = getSum(lines)
    print(result)
