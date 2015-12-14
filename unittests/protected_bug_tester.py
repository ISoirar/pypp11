# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import unittest
import fundamental_tester_base
from pygccxml import declarations
from pyplusplus import code_creators

class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'protected_bug'
    
    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__( 
            self
            , tester_t.EXTENSION_NAME
            , *args )

    def customize(self, mb ):
        access_type_matcher = declarations.access_type_matcher_t
        mb.global_ns.include()
        mb.classes( access_type_matcher('protected') ).exclude()
        mb.vars( access_type_matcher('protected') ).exclude()
        mb.class_( lambda d: d.name.startswith( 'buffered_value' ) ).exclude()
        for cls in mb.classes():
            if declarations.has_destructor(cls) \
               and cls.calldef(lambda d: d.name.startswith('~'), recursive=False).access_type == 'protected':
                print 'protected destructor: ', str( cls )
                cls.constructors().exclude()
                cls.noncopyable =  True
            
    def run_tests( self, module):
        pass
        
def create_suite():
    suite = unittest.TestSuite()    
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
