#! /usr/bin/python
# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys

this_module_dir_path = os.path.abspath ( os.path.dirname( sys.modules[__name__].__file__) )
project_root = os.path.abspath( os.path.join( this_module_dir_path, '..','..' ) )
complete_path = lambda *args: os.path.join( project_root, *args )

class settings:
    pygccxml_path = complete_path( 'pygccxml_dev' )
    pyplusplus_path = complete_path( 'pyplusplus_dev' )
    gccxml_path = complete_path( 'gccxml_bin', 'v09', sys.platform, 'bin' )
    
    @staticmethod
    def setup_environment():
        sys.path.append( settings.pygccxml_path )
        sys.path.append( settings.pyplusplus_path )

settings.setup_environment()
