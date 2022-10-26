'''
    Task:
        Well of Ideas (Easy Version)
'''

# Variables
ideas_1 = [['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']]                         # 'Fail!'
ideas_2 = [['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']]  # 'Publish!'
ideas_3 = [['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']]                      # 'I smell a series!'

# First solution
def is_well_idea(ideas):
    good_count = 0

    for list in ideas:
        for idea in list:
            if idea.lower() == 'good': good_count += 1

    if good_count == 0: return 'Fail!'
    if good_count > 2: return 'I smell a series!'

    return 'Publish!'

# Output
print(is_well_idea(ideas_1))
print(is_well_idea(ideas_2))
print(is_well_idea(ideas_3))
