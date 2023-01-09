# 21. Flatland Space Stations (https://www.hackerrank.com/challenges/flatland-space-stations/problem)

def flatlandSpaceStations(n, c):
    ordered = sorted(c)
    distances = []
    for i in range(1, len(ordered)):
        distances.append(ordered[i] - ordered[i-1])

    for j in range(len(distances)):
        distances[j] = distances[j]//2

    distances.insert(0, ordered[0]-0)
    distances.append((n - 1) - ordered[-1])
    return max(distances)