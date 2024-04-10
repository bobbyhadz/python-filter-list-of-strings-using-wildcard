# Filter a list of strings using a Wildcard in Python

import fnmatch

a_list = ['abc_bobby.csv', 'hadz', '!@#', 'abc_employees.csv']
pattern = 'abc_*.csv'

filtered_list = fnmatch.filter(a_list, pattern)
print(filtered_list)  # 👉️ ['abc_bobby.csv', 'abc_employees.csv']