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

# Second solution
def abbrev_name(name):
    name = name.split(' ')

    first_abbr = name[0][0].upper()
    second_abbr = name[1][0].upper()

    return f'{first_abbr}.{second_abbr}'

# Second solution
def abbrev_name_2(name):
    return name.split()[0][0].upper() + '.' + name.split()[1][0].upper()

# Output
print(abbrev_name(name_1))
print(abbrev_name(name_2))
print(abbrev_name(name_3))
print(abbrev_name(name_4))
print(abbrev_name(name_5))
print(abbrev_name(name_6))

print(abbrev_name_2(name_1))
print(abbrev_name_2(name_2))
print(abbrev_name_2(name_3))
print(abbrev_name_2(name_4))
print(abbrev_name_2(name_5))
print(abbrev_name_2(name_6))
