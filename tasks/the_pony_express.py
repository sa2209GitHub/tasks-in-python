'''
    Task:
        The Pony Express
'''

# Variables
stations_1 = [18, 15]                                               # 1
stations_2 = [43, 23, 40, 13]                                       # 2
stations_3 = [33, 8, 16, 47, 30, 30, 46]                            # 3
stations_4 = [6, 24, 6, 8, 28, 8, 23, 47, 17, 29, 37, 18, 40, 49]   # 4
stations_5 = [24, 45, 24, 21, 34, 25, 15, 30, 48, 41, 45, 43]       # 5

# Solution
def count_riders(stations):
    distance = 0
    riders = 1

    for miles in stations:
        distance += miles
        if distance > 100:
            riders += 1
            distance = miles
    
    return riders

# Output
print(count_riders(stations_1))
print(count_riders(stations_2))
print(count_riders(stations_3))
print(count_riders(stations_4))
print(count_riders(stations_5))
