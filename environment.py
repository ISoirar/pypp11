import os
import sys
import getpass
import platform

this_module_dir_path = os.path.abspath ( os.path.dirname( sys.modules[__name__].__file__) )

class indexing_suite:
    include = os.path.join( this_module_dir_path, 'indexing_suite_v2' )

class boost:
    libs = ''
    include = ''

class python:
    libs = ''
    include = ''

class gccxml:

    gccxml_path = os.path.join( this_module_dir_path, '..', 'gccxml_bin', 'v09', platform.system(), platform.machine(), 'bin' )
    if not os.path.exists( gccxml_path ):
        gccxml_path = os.path.join( this_module_dir_path, '..', 'gccxml_bin', 'v09', sys.platform, 'bin' )

    gccxml_version = '__GCCXML_09__'
    executable = gccxml_path

class scons:
    suffix = ''
    cmd_build = 'scons'
    cmd_clean = 'scons --clean'
    ccflags = []

if 'roman' in getpass.getuser():
    if sys.platform == 'win32':
        scons.suffix = '.pyd'
        scons.ccflags = ['/MD', '/EHsc', '/GR', '/Zc:wchar_t', '/Zc:forScope' ]
        boost.libs = [ r'e:\dev\boost_svn\bin.v2\libs\python\build\msvc-9.0\release\threading-multi' ]
        boost.include = 'e:/dev/boost_svn'
        python.libs = 'c:/program files/python26/libs'
        python.include = 'c:/program files/python26/include'
    else:
        os.nice( 20 )
        print 'test process niceness: 20'
        scons.suffix = '.so'
        scons.ccflags = []
        boost.libs = ['/home/roman/include/libs', '/home/roman/include/lib' ]
        boost.include = '/home/roman/boost_svn'
        python.include = '/usr/include/python2.6'
elif 'root' == getpass.getuser():
    if sys.platform == 'win32':
        scons.suffix = '.pyd'
        scons.ccflags = ['/MD', '/EHsc', '/GR', '/Zc:wchar_t', '/Zc:forScope' ]
        boost.libs = [ 'd:/dev/boost_svn/bin.v2/libs/python/build/msvc-7.1/release/threading-multi' ]
        boost.include = 'd:/dev/boost_svn'
        python.libs = 'e:/python25/libs'
        python.include = 'e:/python25/include'

_my_path = None
try:
    import environment_path_helper
    environment_path_helper.raise_error()
except Exception, error:
    _my_path = os.path.abspath( os.path.split( sys.exc_traceback.tb_frame.f_code.co_filename )[0] )
    if not os.path.exists( os.path.join( _my_path, 'environment.py' ) ):
        #try another guess
        if sys.modules.has_key('environment'):
            _my_path = os.path.split( sys.modules['environment'].__file__ )[0]

try:
    import pygccxml
    print 'pygccxml INSTALLED version will be used'
except ImportError:
    sys.path.append( os.path.join( _my_path, '../pygccxml_dev' ) )
    import pygccxml
    print 'pygccxml DEVELOPMENT version will be used'

import pyplusplus

