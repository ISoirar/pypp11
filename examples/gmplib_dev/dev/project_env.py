import os
import sys
sys.path.append( os.path.join( '..', '..' ) )

from environment import settings, complete_path

class gmp:
    header_file = '/usr/include/gmp.h'
    symbols_file = '/usr/lib/libgmp.so.3.5.0'
    shared_library_file = '/usr/lib/libgmp.so.3.5.0'
    generated_code_dir = complete_path( 'pyplusplus_dev', 'examples', 'gmplib_dev', 'pygmplib' )
