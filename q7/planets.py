# Jacob Duncan & Blaine Mason
def main():
    data = []
    n, m = map(int, input().split())
    for x in range(m):
        rNUM1, rNUM2, routeLength = map(int, input().split())
        data.append([rNUM1, rNUM2, routeLength])
        data.append([rNUM2, rNUM1, routeLength])
    print(data)
    getLongestRequiredRoute(data, n)

def getLongestRequiredRoute(data, n):
    visited = [1]
    adjacent = []
    adjacentWeight = []
    listedValues = []
    currentNodeValue = 1
    for x in range(n+1):
        for path in data:
            if path[0] == currentNodeValue:
                adjacent.append(path[1])
                adjacentWeight.append(path[2])
                print(currentNodeValue, adjacent, adjacentWeight)

        indexOfMin = adjacentWeight.index(min(adjacentWeight))
        print("CURRENT NODE VALUE", currentNodeValue)
        print("ADJACENT[INDEXOFMIN]", adjacent[indexOfMin])
        if adjacent[indexOfMin] in visited:
            i = set(adjacentWeight)
            secondMin = sorted(i)[1]
            print(secondMin)
            indexOfMin = adjacentWeight.index(secondMin)
        listedValues.append(min(adjacentWeight))
        currentNodeValue = adjacent[indexOfMin]
        if adjacent[indexOfMin] not in visited:
            visited.append(currentNodeValue)
        print("VISITED", visited)
        adjacent.clear()
        adjacentWeight.clear()

    print(max(listedValues))

if __name__ == "__main__":
    main()