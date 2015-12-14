# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import ctypes
import shutil
import unittest
import autoconfig
from pyplusplus.module_builder import ctypes_module_builder_t

class ctypes_base_tester_t(unittest.TestCase):

    _module_ref_ = None
    def __init__( self, base_name, *args, **keywd ):
        unittest.TestCase.__init__( self, *args, **keywd )
        self.__base_name = base_name

    @property
    def base_name( self ):
        return self.__base_name

    @property
    def project_dir( self ):
        return os.path.join( autoconfig.data_directory, 'ctypes', self.base_name )

    @property
    def header( self ):
        return os.path.join( self.project_dir, self.base_name + '.h' )

    @property
    def symbols_file( self ):
        ext = '.so'
        prefix = 'lib'
        if 'win32' in sys.platform:
            prefix = ''
            ext = '.map'
        return os.path.join( self.project_dir, 'binaries', prefix + self.base_name + ext )

    @property
    def library_file( self ):
        if 'win32' in sys.platform:
            return os.path.join( self.project_dir, 'binaries', self.base_name + '.dll' )
        else:
            return self.symbols_file

    def customize(self, mb ):
        pass

    def __build_scons_cmd( self ):
        cmd = autoconfig.scons.cmd_build + ' ' + self.base_name
        if autoconfig.cxx_parsers_cfg.gccxml.compiler == 'msvc71':
            cmd  = cmd + ' use_msvc71=True'
        return cmd

    def setUp( self ):
        if self.base_name in sys.modules:
            return sys.modules[ self.base_name ]

        binaries_dir = os.path.dirname( self.symbols_file )
        if os.path.exists( binaries_dir ):
            print '\nrmdir ', binaries_dir
            shutil.rmtree( binaries_dir )

        autoconfig.scons_config.compile( self.__build_scons_cmd(), cwd=autoconfig.this_module_dir_path )
        mb = ctypes_module_builder_t( [self.header], self.symbols_file, autoconfig.cxx_parsers_cfg.gccxml )
        self.customize( mb )        
        mb.build_code_creator( self.library_file )
        mb.write_module( os.path.join( self.project_dir, 'binaries', self.base_name + '.py' ) )
        sys.path.insert( 0, os.path.join( self.project_dir, 'binaries' ) )
        __import__( self.base_name )

    @property
    def module_ref(self):
        return sys.modules[ self.base_name ]




class issues_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'issues', *args, **keywd )

    def test_return_by_value(self):
        x = self.module_ref.return_by_value_t()
        result = x.add( 32, 2 ).result
        self.failUnless( 34 == result, "Expected result 34, got %d" % result)

    def test_free_fun_add( self ):
        self.failUnless( 1977 == self.module_ref.add( 77, 1900 ) )


class enums_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'enums', *args, **keywd )

    def customize( self, mb ):
        mb.enums().include()

    def test(self):
        self.failUnless( self.module_ref.Chisla.nol == 0 )
        self.failUnless( self.module_ref.Chisla.odin == 1 )
        self.failUnless( self.module_ref.Chisla.dva == 2 )
        self.failUnless( self.module_ref.Chisla.tri == 3 )

class opaque_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'opaque', *args, **keywd )

    def customize( self, mb ):
        mb.class_( 'user_data_t' ).opaque = True

    def test(self):
        self.failUnlessRaises( RuntimeError, self.module_ref.user_data_t )
        udt = self.module_ref.create()
        self.failUnless( 1977 == self.module_ref.read_user_data(udt) )
        self.module_ref.destroy( udt )

class include_algorithm_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'include_algorithm', *args, **keywd )

    def customize( self, mb ):
        self.failUnless( mb.global_ns.class_( 'io_marker_t' ).ignore == False )

    def test(self):
        self.failUnless( self.module_ref.io_marker_t )

class anonymous_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'anonymous', *args, **keywd )

    def customize( self, mb ):
        mb.class_( 'rgbai' ).include()

    def test(self):
        c = self.module_ref.color()
        c.r
        c.val

class variables_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'variables', *args, **keywd )

    def customize( self, mb ):
        pass

    def test(self):
        self.module_ref.init()
        self.failUnless( self.module_ref.j.value == 87 )
        self.failUnless( self.module_ref.data.i == 1900 )

        self.failUnless( self.module_ref.data.j == 7 )
        self.failUnless( self.module_ref.data_ptr.contents.i == 11 )

        self.module_ref.j.value = 78
        self.failUnless( self.module_ref.get_value_j() == 78 )

        self.module_ref.data.i = 987
        self.failUnless( self.module_ref.get_value_data() == 987 )

        self.module_ref.data.j = 8
        self.failUnless( self.module_ref.get_value_data_j() == 0 )

        self.module_ref.data.j = 5
        self.failUnless( self.module_ref.get_value_data_j() == 5 )

        self.module_ref.data_ptr.contents.i = 34
        self.failUnless( self.module_ref.get_value_data_p() == 34 )


class function_ptr_as_variable_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'function_ptr_as_variable', *args, **keywd )

    def customize( self, mb ):
        mb.global_ns.typedef('do_smth_fun_t').include()

    @staticmethod
    def identity(v):
        return v
        
    def test(self):
        info = self.module_ref.info()
        info.do_smth_fun = self.module_ref.do_smth_fun_t(self.identity)
        self.failUnless( 21 == self.module_ref.execute_callback( info, 21 ) )
        
class varargs_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'varargs', *args, **keywd )

    def customize( self, mb ):
        pass

    def test(self):
        self.failUnless( 21 == self.module_ref.sum_ints( 3, 5,7,9) )

class circular_references_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'circular_references', *args, **keywd )

    def customize( self, mb ):
        pass

    def test(self):
        bar = self.module_ref.bar_t()
        foo = self.module_ref.foo_t()

        #TODO: add typedefs
        #TODO: sort structs and classes by dependencies
        pass #just test that module could be loaded


class char_ptr_as_binary_data_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'char_ptr_as_binary_data', *args, **keywd )

    def customize( self, mb ):
        mb.treat_char_ptr_as_binary_data = True

    def test(self):
        data = self.module_ref.get_empty()
        self.failUnless( data.contents.size == 0 )
        self.failUnless( not data.contents.bytes )

        data = self.module_ref.get_hello_world()
        self.failUnless( data.contents.size == len( "hello world" ) )
        self.failUnless( data.contents.bytes[0:data.contents.size + 1] == "hello\0world\0" )

class user_code_tester_t( ctypes_base_tester_t ):
    def __init__( self, *args, **keywd ):
        ctypes_base_tester_t.__init__( self, 'user_code', *args, **keywd )
        self.module_top_code = "top = 'top'"
        self.module_bottom_code = "bottom = 'bottom'"
        
    def customize(self, mb ):
        mb.add_module_code( self.module_top_code, tail=False )
        mb.add_module_code( self.module_bottom_code, tail=True )

    def test(self):
        self.failUnless( self.module_ref.top == "top" )
        self.failUnless( self.module_ref.bottom == "bottom" )
        content = []
        for line in file( self.module_ref.__file__ ):
            if line.lstrip().startswith( '#' ) or not line.strip():
                continue
            else:
                content.append( line.rstrip() )
        self.failUnless( content[0] == self.module_top_code )
        self.failUnless( content[-1] == self.module_bottom_code )
        
def create_suite():
    #part of this functionality is going to be deprecated
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(enums_tester_t))
    suite.addTest( unittest.makeSuite(opaque_tester_t))
    suite.addTest( unittest.makeSuite(include_algorithm_tester_t))
    suite.addTest( unittest.makeSuite(anonymous_tester_t))
    suite.addTest( unittest.makeSuite(variables_tester_t))
    suite.addTest( unittest.makeSuite(varargs_tester_t))
    suite.addTest( unittest.makeSuite(circular_references_tester_t))
    suite.addTest( unittest.makeSuite(function_ptr_as_variable_tester_t))
    suite.addTest( unittest.makeSuite(char_ptr_as_binary_data_tester_t))
    suite.addTest( unittest.makeSuite(user_code_tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
