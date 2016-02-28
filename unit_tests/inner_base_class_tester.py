# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import unittest
import fundamental_tester_base
from pygccxml import declarations

class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'inner_base_class'
    
    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__( 
            self
            , tester_t.EXTENSION_NAME
            , *args )

    def customize( self, mb ):
        mb.build_code_creator( self.EXTENSION_NAME )
        foo3 = mb.code_creator.body.creators[0]
        del mb.code_creator.body.creators[0]
        mb.code_creator.body.creators[0].adopt_creator( foo3, 0)
        #mb.class_( 'foo2_t' ).bases[0].access_type = declarations.ACCESS_TYPES.PRIVATE
        #mb.class_( 'foo3_t' ).bases[0].access_type = declarations.ACCESS_TYPES.PRIVATE
        
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
