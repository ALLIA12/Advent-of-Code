import re


def readFile(file_path):
    string_array = []
    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading and trailing whitespace (e.g., newline characters)
            line = line.strip()
            string_array.append(line)

    return string_array


def insert_number_before_word(word, word_to_num):
    for number_word in word_to_num:
        if number_word in word:
            # Insert the numeric value before the number word, also reinsert the number word for edge cases
            # like eightwo, it should give 8, 2 but without reinserting, it just makes it 2
            word = word.replace(number_word, number_word + str(word_to_num[number_word]) + number_word)
    return word


def getOneLineValue(str, word_to_num):
    # Process each word in the input string
    processed_words = [insert_number_before_word(word, word_to_num) for word in re.findall(r'\w+', str)]
    # Extract all numeric values from the processed words
    digits = []
    for word in processed_words:
        digits.extend([int(digit) for digit in re.findall(r'\d', word)])
    summ = digits[0] * 10 + digits[-1]
    return summ


def getSum(string_array, word_to_num):
    sum = 0
    for str in string_array:
        sum += getOneLineValue(str, word_to_num)
    return sum


if __name__ == "__main__":
    string_array = readFile('input.txt')
    # Define a mapping of number words to their numeric values
    word_to_num = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0
    }
    result = getSum(string_array, word_to_num)
    print(result)
