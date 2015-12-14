import os
import sys

import project_env

from pygccxml import utils
from pygccxml import parser
from pygccxml import declarations
from pyplusplus.module_builder import ctypes_module_builder_t


gccxml_cfg = parser.gccxml_configuration_t( gccxml_path=project_env.settings.gccxml_path
                                            , include_paths=project_env.libmemcached.include_paths)

mb = ctypes_module_builder_t( [project_env.libmemcached.header_file]
                              , project_env.libmemcached.symbols_file, gccxml_cfg )

#there is a bug in the code generator
has_varargs = lambda f: f.arguments \
                        and isinstance( f.arguments[-1].type, declarations.ellipsis_t )

mb.calldefs( has_varargs ).exclude()

#libmemcached uses strange convention: every function name starts with __gmp and than, it
#introduces define, which aliass __gmpy to gmpy
#for f in mb.calldefs( lambda x: x.name.startswith('__gmp') ):
#    f.alias = f.name[2:]

#for v in mb.vars( lambda x: x.name.startswith( '__gmp' ) ):
#    v.alias = v.name[2:]

#those structs are private implementation of FILE
#mb.class_( '_IO_FILE' ).opaque = True
#mb.class_( '_IO_marker' ).opaque = True


mb.build_code_creator( project_env.libmemcached.shared_library_file )
mb.write_module( os.path.join( project_env.libmemcached.generated_code_dir, '__init__.py' ) )

