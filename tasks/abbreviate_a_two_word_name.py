'''
    Task:
        Abbreviate
        a Two Word Name
'''

# Variables
name_1 = 'Sam Harris'       # 'S.H'
name_2 = 'Patrick Feenan'   # 'P.F'
name_3 = 'Evan Cole'        # 'E.C'
name_4 = 'P Favuzzi'        # 'P.F'
name_5 = 'David Mendieta'   # 'D.M'
name_6 = 'elon musk'        # 'E.M'

# Solution
def abbrev_name(name):
    name = name.split(' ')
    
    first_abbr = name[0][0].upper()
    second_abbr = name[1][0].upper()

    return f'{first_abbr}.{second_abbr}'

# Output
print(abbrev_name(name_1))
print(abbrev_name(name_2))
print(abbrev_name(name_3))
print(abbrev_name(name_4))
print(abbrev_name(name_5))
print(abbrev_name(name_6))

