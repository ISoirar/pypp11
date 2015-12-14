import os
import sys
#~ from cx_Freeze import setup, Executable

sys.path.append( '..' )
sys.path.append( '../../pygccxml_dev' )

import pygccxml
import pyplusplus

#~ import encodings
#~ encodings_modules = os.listdir( os.path.dirname( encodings.__file__ ) )
#~ encodings_modules = set([ os.path.splitext( m )[0] for m in encodings_modules ])
#~ encodings_modules = map( lambda m: 'encodings.%s.py' % m, encodings_modules )

#~ executable = Executable( "wrap_library.py"
                         #~ , path=['../../pygccxml_dev', '..' ]
                         #~ , includes=encodings_modules
                         #~ , packages=['pygccxml','pyplusplus','encodings'] + encodings_modules )

#~ setup( name = "wrap_library",
        #~ version = "0.1",
        #~ description=r"generates ctypes code from the .dll\.so files",
        #~ executables=[executable] )

    #~ import modulefinder
    #~ import win32com
    #~ root = os.path.dirname( sys.executable )
    #~ modulefinder.AddPackagePath("win32com", os.path.join(root, 'Lib', 'site-packages', 'win32com' ) )
    #~ modulefinder.AddPackagePath("win32com", os.path.join(root, 'Lib', 'site-packages', 'win32comext' ) )


from distutils.core import setup
import py2exe
setup( console=["wrap_library.py"] )
#print py2exe cmd: python freeze.py py2exe
