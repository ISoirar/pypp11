# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import math
import unittest
import fundamental_tester_base
from pygccxml import declarations
from pyplusplus import function_transformers as ft
from pyplusplus.module_builder import call_policies


def remove_const_ref(type):
    """Converts "T const&" into "T &" """
    if declarations.type_traits.is_reference(type):
        t = declarations.cpptypes.reference_t(declarations.type_traits.remove_const(type.base))
        return t
    return type


class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'ft_inout_static_array'

    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__(
            self
            , tester_t.EXTENSION_NAME
            , *args )

    def customize( self, mb ):
        mb.global_ns.calldefs().create_with_signature = True
        
        sum_and_fill = mb.global_ns.calldef( 'sum_and_fill' )
        sum_and_fill.add_transformation( ft.inout_static_array( 'v', 3 ) )
        
        point3d = mb.class_( 'point3d_t' )
        point3d.add_wrapper_code( '' )
        
        swap = point3d.calldefs( lambda d: 'swap' in d.name )
        swap.add_transformation( ft.inout_static_array( 'v', 3 ) )

        
        point3d.mem_fun( 'initialize' ).add_transformation( ft.input_static_array(0, size=3) )
        point3d.mem_fun( 'position' ).add_transformation( ft.output_static_array(0, size=3) )
        
    def run_tests(self, module):
        """Run the actual unit tests.
        """
        point3d = module.point3d_t()
        result = point3d.initialize( [ 1,2,3 ] )
        self.failUnless( result== 1*2*3 and point3d.x == 1 and point3d.y==2 and point3d.z==3 )
        self.failUnless( [1,2,3] == point3d.position() )
        
        self.failUnless( ( 12, [10,10,10] ) == module.sum_and_fill( [2,4,6], 10 ) )
        self.failUnless( [1,2,3] == point3d.swap( [4,5,6] )
                         and [4,5,6] == point3d.position() )
        
def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
