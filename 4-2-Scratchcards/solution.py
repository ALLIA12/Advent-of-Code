def split_card_data(card_string):
    # Splitting the string into card number and data
    card_number, card_data = card_string.split(': ')

    # Further splitting the data based on the '|' character
    before_after_split = card_data.split('|')

    # Converting each part into individual elements and then into integers
    before_array = [int(x) for x in before_after_split[0].split()]
    after_array = [int(x) for x in before_after_split[1].split()]
    card_number = card_number.split(' ')
    return card_number[-1], before_array, after_array


def processCard(card, hashMap, foundCards):
    winning, numbers = hashMap[str(card)]
    counter = card
    for number in numbers:
        if number in winning:
            counter += 1
            # print(f"For card {card} found card {counter}")
            if str(counter) not in hashMap:
                continue
            else:
                foundCards.append(counter)


def getSum(lines):
    hashMap = {}
    foundCards = []
    for line in lines:
        card_number, winning, numbers = split_card_data(line)
        hashMap[card_number] = (winning, numbers)
        foundCards.append(int(card_number))
    sum = 0
    while len(foundCards) != 0:
        currentCard = foundCards.pop(0)

        processCard(currentCard, hashMap, foundCards)
        sum += 1
    return sum


if __name__ == '__main__':
    input_cards = open('input.txt').read()
    lines = input_cards.strip().split('\n')
    result = getSum(lines)
    print(result)
