def readSeeds(line):
    temp = line.split(" ")
    seeds = [int(temp[i]) for i in range(1, len(temp))]
    return seeds


def createMap(position, lines, prevList):
    hashMap = {}
    for val in prevList:
        hashMap[val] = val
    while position < len(lines) and len(lines[position][:]) != 0:
        currentLine = lines[position][:]
        temp = currentLine.split(" ")
        values = [int(temp[i]) for i in range(0, len(temp))]
        dest = values[0]
        source = values[1]
        length = values[2]
        maxSize = source + length
        diff = dest - source
        for val in prevList:
            if source <= val < maxSize:
                hashMap[val] = val + diff
        position += 1
    position += 2

    return position, hashMap


def getLowest(lines):
    position = 0
    listSeeds = readSeeds(lines[position][:])
    position += 3
    print(listSeeds)
    position, soilsMap = createMap(position, lines, listSeeds)
    listSoil = []
    for seed in listSeeds:
        listSoil.append(soilsMap.get(seed, seed))
    print(listSoil)

    position, fertilizerMap = createMap(position, lines, listSoil)
    listFert = []
    for fert in fertilizerMap:
        listFert.append(fertilizerMap.get(fert, fert))
    print(listFert)

    position, waterMap = createMap(position, lines, listFert)
    listWater = []
    for water in waterMap:
        listWater.append(waterMap.get(water, water))
    print(listWater)

    position, lightMap = createMap(position, lines, listWater)
    listLight = []
    for light in lightMap:
        listLight.append(lightMap.get(light, light))
    print(listLight)

    position, temperatureMap = createMap(position, lines, listLight)
    listTemp = []
    for temp in temperatureMap:
        listTemp.append(temperatureMap.get(temp, temp))
    print(listTemp)

    position, humidityMap = createMap(position, lines, listTemp)
    listHumi = []
    for humi in humidityMap:
        listHumi.append(humidityMap.get(humi, humi))
    print(listHumi)

    position, locationMap = createMap(position, lines, listHumi)
    listLoc = []
    for loc in locationMap:
        listLoc.append(locationMap.get(loc, loc))
    print(listLoc)
    return min(listLoc)


if __name__ == '__main__':
    input = open('fullInput.txt').read()
    lines = input.strip().split('\n')
    result = getLowest(lines)
    print(result)
