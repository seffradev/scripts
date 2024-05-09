from typing import Dict, List
import pandas as pd
import sys

categories: Dict[str, List[str]] = {}

def categorize(row: pd.Series):
    for _, value in categories.items():
        if row['Referens'] in value:
            return

    new_category = input('Adding ' + row['Referens'] + ' [' + str(row['Transaktionsdag']) + '](' + str(row['Belopp']) + ' kr)' + ' to category: ')
    if new_category in categories:
        categories[new_category].append(str(row['Referens']))
    else:
        categories[new_category] = [str(row['Referens'])]

def main(in_file, out_file):
    pd.options.mode.copy_on_write = True
    data = pd.read_csv(in_file, encoding='latin1')

    for _, row in data.iterrows():
        categorize(row)

    # write all categories with all rows to Excel file
    with pd.ExcelWriter(out_file) as writer:
        data.loc['Total'] = data.sum(numeric_only=True)
        data.to_excel(writer, sheet_name='All', index=False)
        for category in categories:
            new_data = data[data['Referens'].isin(categories[category])]
            new_data.loc['Total'] = new_data.sum(numeric_only=True)
            new_data.to_excel(writer, sheet_name=category, index=False)

if __name__ == '__main__':
    # get file from args
    if len(sys.argv) < 3:
        print('Usage: python economy-sorter.py <in-file> <out-file>')
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]
    main(in_file, out_file)
