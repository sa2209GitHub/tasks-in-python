'''
    Task:
        Remove
        First and Last
        Character
'''

# Variables
string = 'freedom'  # 'reedo'

# Solution
def remove_first_and_last_character(s):
    return s[1 : len(s) - 1]

# Output
print(remove_first_and_last_character(string))