import re


def readFile(file_path):
    string_array = []
    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading and trailing whitespace (e.g., newline characters)
            line = line.strip()

            string_array.append(line)

    return string_array


def getOneLineValue(str):
    digits = re.findall(r'\d', str)
    sumStr = digits[0] + digits[-1]
    return int(sumStr)


def getSum(string_array):
    sum = 0
    for str in string_array:
        sum += getOneLineValue(str)
    return sum


if __name__ == "__main__":
    string_array = readFile('input.txt')
    result = getSum(string_array)
    print(result)
