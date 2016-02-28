# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import unittest
import fundamental_tester_base
from pygccxml import declarations
from pyplusplus import function_transformers as ft

class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'protected'
    
    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__( 
            self
            , tester_t.EXTENSION_NAME
            , *args )
                                                                    
    def customize(self, mb ):
        def tt( type_ ):
            type_ = declarations.remove_reference( type_ )
            type_ = declarations.remove_const( type_ )
            return declarations.reference_t( type_ )
        mb.classes().always_expose_using_scope = True
        mb.calldefs().create_with_signature = True
        mb.class_( 'Callback' ).add_wrapper_code( '//hhhh' )
        execute = mb.class_( 'Callback' ).mem_fun( 'execute' )
        execute.add_transformation( ft.modify_type(0, tt ) )
        #execute.exclude()

    def create_protected_s_derived_no_override( self, module ):
        class derived(module.protected_v_t):
            def __init__( self ):
                module.protected_v_t.__init__( self )
        return derived()

    def create_protected_s_derived( self, module ):
        class derived(module.protected_v_t):
            def __init__( self ):
                module.protected_v_t.__init__( self )
                
            def get_i(self):
                return 20
                #todo: fix it
                #return super( derived, self ).get_i() * 2
                
        return derived()


    def run_tests(self, module):        
        protected = module.protected_t()
        self.failUnless( protected.get_1() == 1 )

        protected_s = module.protected_s_t()
        self.failUnless( protected_s.get_2() == 2 )
        self.failUnless( module.protected_s_t.get_2() == 2 )

        protected_v = module.protected_v_t()
        self.failUnless( protected_v.get_i() == 10 )

        protected_v_no_override = self.create_protected_s_derived_no_override( module )
        self.failUnless( protected_v_no_override.get_i() == 10 )

        protected_v_override = self.create_protected_s_derived( module )
        self.failUnless( protected_v_override.get_i() == 20 )

        protected_v_d = module.protected_v_derived_t()
        self.failUnless( protected_v_d.get_i() == 10 )


def create_suite():
    suite = unittest.TestSuite()    
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
