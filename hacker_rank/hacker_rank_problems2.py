# 11. Greedy Florist (https://www.hackerrank.com/challenges/greedy-florist/problem?isFullScreen=true)
def getMinimumCost(k, c):
    ordered = sorted(c)
    start = len(ordered) - 1  # starting from the right end of the price list, the more expensive flower should have the lower multipliers
    cost_total = 0
    count = 0
    while start > -1:
        stop = start - k
        if stop < -1:
            stop = -1
        for i in range(start, stop, -1):
            cost_total += ordered[i] * (count + 1)
        count += 1
        start = stop
    return cost_total


# 12. Chocolate Feast (https://www.hackerrank.com/challenges/chocolate-feast/problem?isFullScreen=true)
def chocolateFeast(n, c, m):
    candies = n // c # that's initial number of candies little Bobby can buy with his $$
    wrappers = candies
    while wrappers >= m:
        trade = wrappers // m # extra candies little Bobby can get with the wrappers
        lo_wrappers = wrappers % m # left over wrapper
        candies += trade
        wrappers = trade + lo_wrappers
    return candies


# 13. Between Two Sets (https://www.hackerrank.com/challenges/between-two-sets/problem)
def getTotalX(a, b):
    set_list = []

    for i in range(0, len(b)):
        factors_set = set()
        for j in range(1, int(b[i] ** (1/2)) + 1):
            if b[i] % j == 0:
                factors_set.update([j, b[i]//j])
        set_list.append(factors_set)
    common = set.intersection(*set_list)
    factors_list = [i for i in common if i >= max(a)]

    count = 0
    for k in range(len(factors_list)):
        for l in range(len(a)):
            if factors_list[k] % a[l] != 0:
                break
        else:
            count += 1
    return count


# 14. Happy Ladybug (https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true)
def happyLadybugs(b):
    result = {}
    for i in set(b):
        result[i] = b.count(i)

    if result.get("_", 0) == len(b): # When there are only "_" in the string, always "YES"
        return "YES"
    else: # When number of "_" can range from 0 to < len(b)
        if "_" in b: # When there is "_" in b
            del result["_"]
            for key in result.keys():
                if result.get(key) == 1:
                    return "NO"
            else:
                return "YES"
        else: # When there is no "_" in the string
            for key in result.keys():
                if result.get(key) == 1:
                    return "NO"
                elif key * result.get(key) not in b:
                    return "NO"
            else:
                return "YES"


# 15. Fair Rations (https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true)
def fairRations(B):
    odd_indices = [i for i in range(len(B)) if B[i] % 2 != 0]
    loaves = 0
    if len(odd_indices) % 2 != 0:
        return "NO"
    else:
        for j in range(0, len(odd_indices), 2):
            loaves += 2 * (odd_indices[j+1] - odd_indices[j])
        return str(loaves)


# 16. Strong Password (https://www.hackerrank.com/challenges/strong-password/problem)
def minimumNumber(n, password):
    count = 0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    for i in range(len(password)):
        if password[i] in numbers:
            count += 1
            break
    for j in range(len(password)):
        if password[j] in lower_case:
            count += 1
            break
    for k in range(len(password)):
        if password[k] in upper_case:
            count += 1
            break
    for l in range(len(password)):
        if password[l] in special_characters:
            count += 1
            break

    return max(4-count, 6-n)


# 17. Strange Counter (https://www.hackerrank.com/challenges/strange-code/problem?isFullScreen=true)

def strangeCounter(t):
    initial = 3
    count = 1
    while t - initial > 0:
        count += 1
        t -= initial
        initial = 3 * 2 ** (count -1)

    return initial - (t - 1)

# 18. Almost Sorted (https://www.hackerrank.com/challenges/almost-sorted/problem?isFullScreen=true)
def almostSorted(arr):
    ordered = sorted(arr)

    original_dict = {}
    for i, v in enumerate(arr, 1):
        original_dict[v] = i

    count = 0
    for i in range(len(ordered)):
        if i + 1 != original_dict.get(ordered[i]):
            count += 1
            if count == 1:
                operation_ind = [i+1, original_dict.get(ordered[i])]

    if count == 0:
        print("yes")
    elif count == 2:
        print("yes \nswap", operation_ind[0], operation_ind[1])
    else:
        if operation_ind[1] - (count - 1) == operation_ind[0]:
            print("yes \nreverse", operation_ind[0], operation_ind[1])
        else:
            print("no")


# 19. Goodland Electricity (https://www.hackerrank.com/challenges/pylons/problem?isFullScreen=true)
def pylons(k, arr):
    plant_ind = [i for i in range(len(arr)) if arr[i] == 1]

    for j in range(0, len(plant_ind)):
        # j is the index of the city that could have a power plant and
        # if the very first city is >= k away from the end, it wouldn't be able to cover all the cities at the end
        if j == 0 and plant_ind[j] >= k:
            return -1
        elif j == len(plant_ind) - 1 and (len(arr) - plant_ind[j]) > k:
            return -1
        else:
            if (plant_ind[j] - plant_ind[j - 1]) > (2 * (k - 1)):
                return -1
    else:
        location = k - 1
        count = 0
        while location < plant_ind[-1]:
            for j in range(0, len(plant_ind)):
                if plant_ind[j] > location:
                    location = (plant_ind[j-1] + (2*k -1))
                    count += 1

        return count + 1