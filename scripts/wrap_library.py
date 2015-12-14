import os
import sys
import types

try:
    import pygccxml
except ImportError, err:
    sys.path.append( '../../pygccxml_dev' )
    import pygccxml

try:
    import pyplusplus
except ImportError, err:
    sys.path.append( '..' )
    import pyplusplus
    
import optparse

parser = optparse.OptionParser()
parser.add_option( '-c'
                   , '--compiler-config'
                   , dest="compiler_config"
                   , help="pygccxml configuration file for GCCXML"
                   , type="string"
                   , action="store"
                   , default=os.path.abspath( os.path.join( os.curdir, 'gccxml.cfg' ) ) )

parser.add_option( '-g'
                   , '--generate-config'
                   , dest="generate_config"
                   , help="generates an example of the compiler configuration file (gccxml.cfg) in the current working directory"
                   , action="store_true"
                   , default=False )

parser.add_option( '-s'
                   , '--source-file'
                   , dest="source_file"
                   , help="source file name - should be specified"
                   , type="string"
                   , action="store" )

parser.add_option( '-d'
                   , '--shared-library'
                   , dest="shared_library"
                   , help=r"shared\dynamic library file name  - should be specified"
                   , type="string"
                   , action="store" )

parser.add_option( '-o'
                   , '--output-file'
                   , dest="output_file"
                   , help="output file name, if not specified stdout will be used"
                   , type="string"
                   , action="store"
                   , default=sys.stdout )

def generate_code( options ):
    gccxml = pygccxml.parser.load_gccxml_configuration( options.compiler_config )
    #~ import pdb
    #~ pdb.set_trace()
    fc = pygccxml.parser.create_source_fc( options.source_file )    
    mb = pyplusplus.module_builder.ctypes_module_builder_t( [ fc ], options.shared_library, gccxml )
    mb.build_code_creator( options.shared_library )
    if isinstance( options.output_file, types.StringTypes ):    
        mb.write_module( options.output_file )
    else:
        print mb.code_creator.create()

if __name__ == '__main__':
    options, unused = parser.parse_args(sys.argv[1:])
    
    if options.generate_config:
        f_path = os.path.abspath( os.path.join( os.curdir, 'gccxml.cfg' ) )
        f = file( f_path, 'w+' )
        f.write( pygccxml.parser.gccxml_configuration_example )
        f.close()
        print 'file: "%s" was generated' % f_path
    else:
        if None is options.source_file:
            parser.error("You have to specify source file")
        if None is options.shared_library:
            parser.error(r"You have to specify shared\dynamic library file")
        else:
            generate_code( options )
        
        
