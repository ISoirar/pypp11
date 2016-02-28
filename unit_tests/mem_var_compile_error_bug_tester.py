# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import unittest
import fundamental_tester_base
from pyplusplus.module_builder import call_policies

class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'mem_var_compile_error_bug'

    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__(
            self
            , tester_t.EXTENSION_NAME
            , *args )

    def customize(self, mb ):
        opaqueDecls = {
                'Path': ['reverse'],
                'RailTracking': ['getPath'],
                'Track': ['getPath', 'getDefaultPath']
                }

        mb.class_('Path').include()

        for decl in opaqueDecls.items():
            cls = mb.class_(decl[0])
            for methodName in decl[1]:
                cls.member_function(methodName).call_policies = call_policies.return_value_policy(call_policies.return_opaque_pointer);

    def run_tests(self, module):
        pass

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
