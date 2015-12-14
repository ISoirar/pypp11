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
    EXTENSION_NAME = 'indexing_suites2_support'

    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__(
            self
            , tester_t.EXTENSION_NAME
            , indexing_suite_version=2
            , *args)

    def customize(self, generator):
        fvector = generator.global_ns.typedef( 'foo_vector' )
        fvector = declarations.remove_declarated( fvector.type )
        fvector.indexing_suite.call_policies \
            =  module_builder.call_policies.return_internal_reference()

    def run_tests( self, module):
        v = module.foo_vector()
        f = module.foo()
        f.bar = 0
        v.append(f)
        self.failUnless( v[0].bar == 0 )
        v[0].bar = 10
        self.failUnless( v[0].bar == 10 )

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
