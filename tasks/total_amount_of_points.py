'''1
    Task:
        Total Amount of Points
'''

# Variables
games1 = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']    # 30
games2 = ['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']    # 10
games3 = ['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']    # 0
games4 = ['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']    # 15
games5 = ['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']    # 12

# First solution
def count_points(games):
    total = 0

    for scores in games:
        scores_str = scores.split(':')
        first_score, second_score = int(scores_str[0]), int(scores_str[1])

        if first_score > second_score:
            total += 3
            
        if first_score == second_score:
            total += 1

    return total

# Second solution
def count_points_2(args):
    return 0

# Output
print(count_points(games1))
print(count_points(games2))
print(count_points(games3))
print(count_points(games4))
print(count_points(games5))
