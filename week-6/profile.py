# import logging
# import csv
# from collections import Counter, defaultdict

# file_path = 'data/Indian_Web_Series_2014_2025_Episodes_Clean.csv'

# with open(file_path, encoding='utf-8', newline='') as csv_open:
#     csv_reader = csv.DictReader(csv_open)
#     csv_output = list(csv_reader)
#     csv_fieldnames = csv_reader.fieldnames
#     column_blank = defaultdict(int)
#     column_values = defaultdict(list)
#     most_common = Counter(dict(column_values)).most_common(3)
#     for row in csv_output:
#         for col in csv_fieldnames:
#             if row[col] == '':
#                 column_blank[col] +=1

#     for row in csv_output:
#         for key, val in row.items():
#             column_values[key].append(val)

#     print(csv_reader.fieldnames)
#     print(len(csv_output))
#     print(dict(column_blank))
#     #print(csv_output)
#     print(most_common)

import logging
import csv
from collections import Counter, defaultdict

file_path = 'data/Indian_Web_Series_2014_2025_Episodes_Clean.csv'

def profiling_csv(file_path, top_n):
    with open(file_path, encoding='utf-8', newline='') as csv_open:
        csv_reader = csv.DictReader(csv_open)
        csv_fieldnames = csv_reader.fieldnames
        column_blank = {col: 0 for col in csv_fieldnames}
        column_values = {col: Counter() for col in csv_fieldnames}
        row_count = 0
        for row in csv_reader:
            row_count += 1
            for col in csv_fieldnames:
                val = row[col].strip()
                if val == '':
                    column_blank[col] += 1
                else:
                    column_values[col][val] += 1
                    
    most_common = {col: c.most_common(top_n) for col, c in column_values.items()}
    return csv_fieldnames, row_count, column_blank, most_common


if __name__ == '__main__':
    csv_fieldnames, row_count, column_blank, most_common = profiling_csv(file_path, top_n=3)
    print(csv_fieldnames)
    print(row_count)
    print({col:val for col,val in column_blank.items() if val})
    for col,top in most_common.items():
        print(col, top)