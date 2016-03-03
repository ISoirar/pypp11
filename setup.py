# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE.md or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import sys, os, os.path
from distutils import sysconfig
from distutils.core import setup
from distutils.cmd import Command

setup( name = "Py++11",
       version = "0.1.0",
       description="Py++11 is a framework of components for creating C++ code generator for pybind11 library",
       author="Rarios",
       author_email="rarios.dev@gmail.com",
       url='https://github.com/IAmRarios/pypp11',
       scripts = ["scripts/pyplusplus_gui",
                  "scripts/pyplusplus_gui.pyw"],
       packages=[ 'pypp11',
                  'pypp11.file_writers',
                  'pypp11.code_creators',
                  'pypp11.creators_factory',
                  'pypp11.code_repository',
                  'pypp11.code_repository.indexing_suite',
                  'pypp11.decl_wrappers',
                  'pypp11.module_builder',
                  'pypp11.utils',
                  'pypp11.function_transformers',
                  'pypp11._logging_',
                  'pypp11.messages'] )
