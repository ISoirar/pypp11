# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import sys, os, os.path
from distutils import sysconfig
from distutils.core import setup
from distutils.cmd import Command

setup( name = "Py++",
       version = "1.0.0",
       description="Py++ is a framework of components for creating C++ code generator for Boost.Python library",
       author="Roman Yakovenko",
       author_email="roman.yakovenko@gmail.com",
       url='http://www.language-binding.net/pyplusplus/pyplusplus.html',
       scripts = ["scripts/pyplusplus_gui",
                  "scripts/pyplusplus_gui.pyw"],
       packages=[ 'pyplusplus',
                  'pyplusplus.file_writers',
                  'pyplusplus.code_creators',
                  'pyplusplus.creators_factory',
                  'pyplusplus.code_repository',
                  'pyplusplus.code_repository.indexing_suite',
                  'pyplusplus.decl_wrappers',
                  'pyplusplus.module_builder',
                  'pyplusplus.utils',
                  'pyplusplus.function_transformers',
                  'pyplusplus._logging_',
                  'pyplusplus.messages'] )
