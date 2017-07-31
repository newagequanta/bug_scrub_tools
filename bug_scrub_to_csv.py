'''
Version 4:
    1. Two new columns
        a. CDETS URL of the bug
        b. CloudApps URL of the bug
Version 4:
    1. Broken up into 3 functions:
        a. open_text_file - Create a file object
        b. read_text_file - An object generator (read docstring)
        c. create_csv - Create the final CSV
Version 3:
    1. File name is asked for in input
Version 2:
    1. for function going thru list is made more efficient
    2. CSV module used to output to CSV file
'''

def open_text_file(filename):
    '''
    INPUT - Filename in CWD
    RETURN - open file "object"
    '''

    return open(filename, 'r')

def read_text_file(fileobject):
    '''
    INPUT - Python File Object
    YIELD - Only non-empty lines
    A generator to read the raw text file and return only non-empty lines
    '''

    for line in fileobject:
        if line.strip():
            yield line.strip()

def create_csv(input_filename, output_filename):
    '''
    INPUT - A text file of the bugscrub, Name of the CSV file
    OUTPUT - A CSV file created in the current directory
    '''
    import csv

    #Create a read object by:
        #First calling the open_text_file on input_filename
        #Then callin gthe read_text_file with the above object

    read_object = read_text_file(open_text_file(input_filename))

    #Variable to store the previous line, used for logic check later
    prev_line = ''

    #Variables to store the URL prefixes for CDETS and CloudApps
    #=HYPERLINK is added to ensure a hyperlink appears in CSV and not just test
    cdets_pfix = '=HYPERLINK("https://cdetsng.cisco.com/webui/#view='
    capps_pfix = '=HYPERLINK("https://bst.cloudapps.cisco.com/bugsearch/bug/'
    capps_pfix2 = '=HYPERLINK("https://quickview.cloudapps.cisco.com/quickview/bug/'

    #create the list of lists with Header Only, relevant records added later
    all_records = [['Identifier', 'AS Severity', 'Headline', 'CDETS Link',
                    'CloudApps Link', 'CloudApps Alternate Link']]

    for line in read_object:
        if prev_line.startswith('Identifier'):
            #The line object now contains the Bug-ID
            current_record = []

            #The CDETS and CloudApps URLs are created with the prefix+Bug-ID
            cdets_url = '{}{}")'.format(cdets_pfix, line)
            capps_url = '{}{}")'.format(capps_pfix, line)
            capps_url2 = '{}{}")'.format(capps_pfix2, line)

            current_record.append(line)
            next(read_object)
            current_record.append(next(read_object).split(': ')[1])
            for _ in range(3):
                next(read_object)
            current_record.extend([next(read_object), cdets_url, capps_url,
                                   capps_url2])
            all_records.append(current_record)
        prev_line = line

    read_object.close()

    output_file = csv.writer(open(output_filename, 'w'), delimiter=',',
                             quoting=csv.QUOTE_ALL)
    for record in all_records:
        output_file.writerow(record)

def main():
    '''
    Main function
    '''
    input_filename = input('Which file in the CWD do you want to open? ')
    output_filename = input('What do you want to name the CSV file in the CWD? '
                           )
    create_csv(input_filename, output_filename)

main()
