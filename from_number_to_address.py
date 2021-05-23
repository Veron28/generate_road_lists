
def from_number_to_address(start, mass):
    oneday = [[start[i - 1], start[i]] for i in range(1, len(start))]
    for i in range(len(oneday)):
        oneday[i] = [mass[oneday[i][0]][2], mass[oneday[i][1]][2]]
    return oneday