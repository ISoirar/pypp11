# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import unittest
import autoconfig
import fundamental_tester_base
from pyplusplus import code_creators

if 'linux' in sys.platform:
    try:
        from ctypes import RTLD_NOW, RTLD_GLOBAL
    except ImportError:
        RTLD_NOW = 2
        RTLD_GLOBAL = 256
    sys.setdlopenflags(RTLD_NOW | RTLD_GLOBAL)

class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__( self, self.EXTENSION_NAME, indexing_suite_version=2, *args  )

    def run_tests(self, module):
        v = module.create_vector()
        for i in v:
            i += 1
        for i in v:
            i += 1

class tester_a_t(tester_t):
    EXTENSION_NAME = 'indexing_suites_v2_bug_a'
    def __init__( self, *args ):
        tester_t.__init__( self, *args )


class tester_b_t(tester_t):
    EXTENSION_NAME = 'indexing_suites_v2_bug_b'
    def __init__( self, *args ):
        tester_t.__init__( self, *args )

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_a_t))
    suite.addTest( unittest.makeSuite(tester_b_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
