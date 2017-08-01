'''
Version 2:
    Improved the file read to ensure the file object is closed properly
Program to find the following:
    1. Accept two CSVs - New and Old
    2. Create two CSVs:
        a. Records added to the New CSV
        b. Records removed from the OLD CSV
        b. Total number of differences
'''

def create_csv_obj(filename):
    '''
    INPUT - Filename in CWD
    RETURN - open file "object"
    '''
    import csv

    return csv.reader(filename)

def create_diff_csvs(csv_old, csv_new):
    '''
    INPUT - 2 CSV file objects
    OUTPUT:
        Total number of differences
        CSV with records added
        CSV with records deleted
    '''
    import csv
    dict_old = {}
    dict_new = {}

    records_added = csv.writer(open('records_added.csv', 'w'), delimiter=',',
                               quoting=csv.QUOTE_ALL)
    records_deleted = csv.writer(open('records_deleted.csv', 'w'), delimiter=',',
                                 quoting=csv.QUOTE_ALL)

    for line in csv_old:
        dict_old[line[0]] = line[1:]

    for line in csv_new:
        dict_new[line[0]] = line[1:]

    for line in dict_new:
        if line not in dict_old:
            records_added.writerow([line]+dict_new[line])
        else:
            del dict_old[line]

    for line in dict_old:
        records_deleted.writerow([line]+dict_old[line])

def main():
    '''
    Main caller function
    '''

    csv_old = input('Input the name of old CSV in CWD: ')
    csv_new = input('Input the name of new CSV in CWD: ')

    with open(csv_old, 'r') as fo_old, open(csv_new, 'r') as fo_new:
        create_diff_csvs(create_csv_obj(fo_old), create_csv_obj(fo_new))

main()
