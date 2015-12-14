# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

"""updates code repository"""

import os
import sys

header_tmpl = \
'''# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

"""
This file contains indexing suite v2 code
"""

file_name = "%(file_path)s"

code = \
"""%(code)s

"""
'''

init_code = [
'''# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

"""
code repository for Indexing Suite V2 - std containers wrappers
"""

all = []
''']

pyplusplus_dev_root = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
source_dir = os.path.join( pyplusplus_dev_root, 'indexing_suite_v2', 'indexing_suite' )
target_dir = os.path.join( pyplusplus_dev_root, 'pyplusplus', 'code_repository', 'indexing_suite' )

if not os.path.exists( target_dir ):
    os.mkdir( target_dir )

for f in os.listdir( source_dir ):
    name, ext = os.path.splitext( f )
    if  ext != '.hpp':
        print 'file "%s" was skipped' % f
        continue
    else:
        print 'converting file "%s"' % f
    file_path = 'indexing_suite/' + f
    code = file( os.path.join( source_dir, f ), 'r' ).read()
    py_name = name + '_header'
    py_file = file( os.path.join( target_dir, py_name + '.py' ), 'w+' )
    py_file.write( header_tmpl % dict( file_path=file_path, code=code ) )
    py_file.close()
    init_code.append( 'import %s' % py_name )
    init_code.append( 'all.append( %s )' % py_name )
    init_code.append( '' )

init_code.append( 'headers = map( lambda f: f.file_name, all )' )

print 'creating __init__.py file'

init_file = file( os.path.join( target_dir, '__init__.py' ), 'w+' )
init_file.write( '\n'.join( init_code ) )
init_file.close()







