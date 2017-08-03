'''
The hook for BDB
This will call create_csv in bug_scrub_to_csv module
'''
print(__name__)
from . import __init__
def main():
    '''
    Main function
    '''
    input_filename = input('Which file in the CWD do you want to open? ')
    output_filename = input('What do you want to name the CSV file in the CWD? '
                           )
    __init__.task(input_filename, output_filename)

main()
