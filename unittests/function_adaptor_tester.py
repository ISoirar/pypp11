# -*- coding: utf-8 -*-
# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import unittest
import fundamental_tester_base
from pyplusplus import code_creators

class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'function_adaptor'

    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__(
            self
            , tester_t.EXTENSION_NAME
            , *args )

    def customize(self, mb ):
        for suffix in [ 'zero', 'one', 'two' ]:
            funs = mb.calldefs( 'get_' + suffix )
            funs.adaptor = 'PYPP_IDENTITY'
            funs.create_with_signature = False
            mfuns = mb.global_ns.mem_funs( 'get_' + suffix, allow_empty=True )
            mfuns.add_default_precall_code( '//add_default_precall_code' )
            mfuns.add_override_precall_code( '//add_override_precall_code' )
            mfuns.add_override_native_precall_code( '//add_override_native_precall_code' )
        mb.class_('base3_t' ).add_wrapper_code( '//just a comment to force Py++ create wrapper' )
        mb.mem_fun( '::derived_t::get_two' ).alias = 'get2'
        Foo = mb.class_('Foo')
        for f in [ 'virtual_public', 'virtual_protected' ]:
            f = Foo.mem_fun( f )
            f.add_default_precall_code( '//add_default_precall_code' )
            f.add_override_precall_code( '//add_override_precall_code' )
            f.add_override_native_precall_code( '//add_override_native_precall_code' )

    def create_foo_derived(self, module):
        class pyfoo( module.Foo ):
            def __init__( self ):
                module.Foo.__init__( self )

            def virtual_protected( self ):
                return 3
        return pyfoo( );

    def create_foo_derived2(self, module):
        class pyfoo2( module.Foo ):
            def __init__( self ):
                module.Foo.__init__( self )

            def virtual_protected( self ):
                return module.Foo.virtual_protected( self )
        return pyfoo2( );

    def run_tests( self, module):
        foo = module.foo_t()
        self.failUnless( foo.get_zero() == 0 )
        self.failUnless( foo.get_two() == 2 )
        self.failUnless( module.foo_t.get_two() == 2 )
        self.failUnless( module.get_one() == 1 )

        pyfoo = self.create_foo_derived( module )
        self.failUnless( pyfoo.virtual_public() == 1 )
        self.failUnless( pyfoo.virtual_protected() == 3 )
        self.failUnless( pyfoo.call_virtual_protected() == 3 )

        pyfoo2 = self.create_foo_derived2( module )
        self.failUnless( pyfoo2.virtual_public() == 1 )
        self.failUnless( pyfoo2.virtual_protected() == 2 )
        self.failUnless( pyfoo2.call_virtual_protected() == 2 )

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
