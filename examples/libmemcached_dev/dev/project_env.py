import os
import sys
sys.path.append( os.path.join( '..', '..' ) )

from environment import settings, complete_path

clib_sources = complete_path( 'pyplusplus_dev', 'examples', 'libmemcached_dev', 'libmemcached-0.31' )

class libmemcached:
    include_paths = [ clib_sources ]
    header_file = os.path.join( clib_sources, 'libmemcached/memcached.h' )
    symbols_file = os.path.join( clib_sources, 'libmemcached/.libs/libmemcached.so' )
    shared_library_file = os.path.join( clib_sources, 'libmemcached/.libs/libmemcached.so' )
    generated_code_dir = complete_path( 'pyplusplus_dev', 'examples', 'libmemcached_dev', 'pymemcached' )
