'''
    Task:
        Well of Ideas (Easy Version)
'''

# Variables
from operator import is_


ideas_1 = ['bad', 'bad', 'bad']                                                 # 'Fail!'
ideas_2 = ['good', 'bad', 'bad', 'bad', 'bad']                                  # 'Publish!'
ideas_3 = ['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']    # 'I smell a series!'

# First solution
def is_well_idea(ideas):
    if 'good' not in ideas:
        return 'Fail!'
    else:
        good_ideas_counter = 0

        for idea in ideas:
            if idea == 'good':
                good_ideas_counter += 1
    
    if good_ideas_counter > 2:
        return 'I smell a series!'

    return 'Publish!'

# Second solution
def is_well_idea_2(ideas):
    if ideas.count('good') == 0:  return 'Fail!'
    if ideas.count('good') > 2:   return 'I smell a series!'
    return 'Publish!'

# Output
print(is_well_idea(ideas_1))
print(is_well_idea(ideas_2))
print(is_well_idea(ideas_3))

print(is_well_idea_2(ideas_1))
print(is_well_idea_2(ideas_2))
print(is_well_idea_2(ideas_3))

