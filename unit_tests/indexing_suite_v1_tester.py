# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import unittest
import autoconfig
from pyplusplus import utils
import fundamental_tester_base
from pygccxml import declarations
from pyplusplus import module_builder
from pyplusplus.module_builder import call_policies

class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'indexing_suite_v1'

    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__(
            self
            , tester_t.EXTENSION_NAME
            , indexing_suite_version=1
            , *args )
        self.files = []

    def customize( self, mb ):
        v = mb.class_( lambda x: x.name.startswith( 'vector' ) )
        v.exclude()

    def run_tests(self, module):
        x = module.get_empty()
        try:
            for i in x:
                print i
            self.fail( "TypeError exception was not raised" )
        except TypeError:
            pass

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
