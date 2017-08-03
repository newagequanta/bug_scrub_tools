'''
The hook for BDB, BDB calls the task() function via GUI
This will call create_csv in bug_scrub_to_csv module
'''
#code.py is the file with all the main functions
from . import code
__copyright__ = "Copyright (c) 2017 Cisco Systems. All rights reserved."
def task(Env, input_filename, output_filename):
    """
    Accepts a bug scrub from GDC (in unicode-8) and produces a CSV with relevant information 
    
    This task is run by the bdblib library, full doc and examples at: 
    https://scripts.cisco.com/doc/
    Browse more examples in BDB starting with "bdblib_":
    https://scripts.cisco.com/ui/browse/used/0/bdblib_
    """
    
    #create_csv is the function inside code that accepts filenames and starts
    #procss
    code.create_csv(input_filename, output_filename)
    return 'Task Finished, download file from your files'
