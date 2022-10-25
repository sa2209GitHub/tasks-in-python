'''
    Task:
        Remove an Exclamation Mark
        from the end of String
'''

# Variables
str_1 = 'Hi!'        # 'Hi'
str_2 = 'Hi!!!'      # 'Hi!!'
str_3 = '!Hi'        # '!Hi'
str_4 = '!Hi!'       # '!Hi'
str_5 = 'Hi! Hi!'    # 'Hi! Hi'
str_6 = 'Hi'         # 'Hi'

# Solution
def remove(s):
    return s if s[-1] != '!' else s[0:-1]

# Output
print(remove(str_1))
print(remove(str_2))
print(remove(str_3))
print(remove(str_4))
print(remove(str_5))
print(remove(str_6))