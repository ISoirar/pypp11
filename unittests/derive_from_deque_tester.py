# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import unittest
import fundamental_tester_base
from pygccxml import declarations
from pyplusplus import module_builder


class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'derive_from_deque'

    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__(
            self
            , tester_t.EXTENSION_NAME
            , indexing_suite_version=2
            , *args)

    def customize(self, mb):
        pass
        #~ mb.class_( 'deque<C>' ).include()


    def run_tests( self, module):
        c = module.C( 1,2)
        f = module.F()
        f.append(c)
        c2 = f[0]
        self.failUnless( c2.a_ == c.a_ and c2.b_ == c.b_ )

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
