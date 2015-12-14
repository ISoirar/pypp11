# -*- coding: UTF-8 -*-

import os
import unittest
import autoconfig
import pygccxml
from pygccxml import parser
from pygccxml import declarations
from pyplusplus import code_creators
from pyplusplus import creators_factory
from pyplusplus import module_builder
from pyplusplus import utils as pypp_utils
from pyplusplus import function_transformers as ft


class tester_t( unittest.TestCase ):
    def test(self):
        mb = module_builder.module_builder_t(
                        [ module_builder.create_text_fc( 'struct x{};' ) ]
                        , gccxml_path=autoconfig.gccxml.executable
                        , encoding='UTF-8'
                        , compiler=autoconfig.cxx_parsers_cfg.gccxml.compiler)

        mb.build_code_creator( module_name='unicode_bug' )
        mb.code_creator.license = "//абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        mb.write_module( os.path.join( autoconfig.build_dir, 'unicode_bug.cpp' ) )


def create_suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
